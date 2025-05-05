.DEFAULT_GOAL := all

# M1 macs may need to switch back to x86, until arm releases are available
EMULATE_X86 =
ifeq ($(shell uname -sm),Darwin arm64)
EMULATE_X86 = arch -x86_64
endif

OS = $(shell uname -s)
ARCH = $(shell $(EMULATE_X86) uname -m)

# current (when committed) version of Go used in CI, and ideally also our docker images.
# this generally does not matter, but can impact goimports output.
# for maximum stability, make sure you use the same version as CI uses.
#
# this can _likely_ remain a major version, as fmt output does not tend to change in minor versions,
# which will allow findstring to match any minor version.
EXPECTED_GO_VERSION := go1.17
CURRENT_GO_VERSION := $(shell go version)
ifeq (,$(findstring $(EXPECTED_GO_VERSION),$(CURRENT_GO_VERSION)))
# if you are seeing this warning: consider using https://github.com/travis-ci/gimme to pin your version
$(warning Caution: you are not using CI's go version. Expected: $(EXPECTED_GO_VERSION), current: $(CURRENT_GO_VERSION))
$(warning If you have recently changed your version: make sure to clean and rebuild, as pre-built tools generally inherit Go's formatting for that version.)
endif

BIN := .bin
$(BIN):
	@mkdir -p $@

# https://docs.buf.build/
# changing BUF_VERSION will automatically download and use the specified version.
BUF_VERSION = 0.36.0
BUF_URL = https://github.com/bufbuild/buf/releases/download/v$(BUF_VERSION)/buf-$(OS)-$(ARCH)
# use BUF_VERSION_BIN as a bin prerequisite, not "buf", so the correct version will be used.
BUF_VERSION_BIN = buf-$(BUF_VERSION)
$(BIN)/$(BUF_VERSION_BIN): | $(BIN)
	@echo "downloading buf $(BUF_VERSION)"
	@curl -sSL $(BUF_URL) -o $@
	@chmod +x $@

PROTO_ROOT := proto
PROTO_FILES = $(shell find ./$(PROTO_ROOT) -name "*.proto")
PROTO_DIRS = $(sort $(dir $(PROTO_FILES)))
proto-lint: $(PROTO_FILES) $(BIN)/$(BUF_VERSION_BIN)
	@$(BIN)/$(BUF_VERSION_BIN) lint

# https://www.grpc.io/docs/languages/go/quickstart/
# protoc-gen-gogofast (yarpc) are versioned via tools.go + go.mod (built above) and will be rebuilt as needed.
# changing PROTOC_VERSION will automatically download and use the specified version
PROTOC_VERSION = 3.14.0
PROTOC_URL = https://github.com/protocolbuffers/protobuf/releases/download/v$(PROTOC_VERSION)/protoc-$(PROTOC_VERSION)-$(subst Darwin,osx,$(OS))-$(ARCH).zip
# the zip contains an /include folder that we need to use to learn the well-known types
PROTOC_UNZIP_DIR = $(BIN)/protoc-$(PROTOC_VERSION)-zip
# use PROTOC_VERSION_BIN as a bin prerequisite, not "protoc", so the correct version will be used.
# otherwise this must be a .PHONY rule, or the buf bin / symlink could become out of date.
PROTOC_VERSION_BIN = protoc-$(PROTOC_VERSION)
$(BIN)/$(PROTOC_VERSION_BIN): | $(BIN)
	@echo "downloading protoc $(PROTOC_VERSION)"
	@# recover from partial success
	@rm -rf $(BIN)/protoc.zip $(PROTOC_UNZIP_DIR)
	@# download, unzip, copy to a normal location
	@curl -sSL $(PROTOC_URL) -o $(BIN)/protoc.zip
	@unzip -q $(BIN)/protoc.zip -d $(PROTOC_UNZIP_DIR)
	@cp $(PROTOC_UNZIP_DIR)/bin/protoc $@

$(BIN)/protoc-gen-gogofast: go.mod | $(BIN)
	go build -o $(BIN)/protoc-gen-gogofast github.com/gogo/protobuf/protoc-gen-gogofast

$(BIN)/protoc-gen-yarpc-go: go.mod | $(BIN)
	go build -o $(BIN)/protoc-gen-yarpc-go go.uber.org/yarpc/encoding/protobuf/protoc-gen-yarpc-go

PROTO_GO_OUT := go/proto
proto-go: $(PROTO_FILES) $(BIN)/$(PROTOC_VERSION_BIN) $(BIN)/protoc-gen-gogofast $(BIN)/protoc-gen-yarpc-go
	@mkdir -p $(PROTO_GO_OUT)
	@echo "protoc..."
	@$(foreach PROTO_DIR,$(PROTO_DIRS),$(EMULATE_X86) $(BIN)/$(PROTOC_VERSION_BIN) \
		--plugin $(BIN)/protoc-gen-gogofast \
		--plugin $(BIN)/protoc-gen-yarpc-go \
		-I=$(PROTO_ROOT) \
		-I=$(PROTOC_UNZIP_DIR)/include \
		--gogofast_out=Mgoogle/protobuf/duration.proto=github.com/gogo/protobuf/types,Mgoogle/protobuf/field_mask.proto=github.com/gogo/protobuf/types,Mgoogle/protobuf/timestamp.proto=github.com/gogo/protobuf/types,Mgoogle/protobuf/wrappers.proto=github.com/gogo/protobuf/types,paths=source_relative:$(PROTO_GO_OUT) \
		--yarpc-go_out=$(PROTO_GO_OUT) \
		$$(find $(PROTO_DIR) -name '*.proto');\
	)
	@rm -r $(PROTO_GO_OUT)/api
	@rm -r $(PROTO_GO_OUT)/admin
	@mv $(PROTO_GO_OUT)/uber/cadence/* $(PROTO_GO_OUT)
	@rm -r $(PROTO_GO_OUT)/uber

all: proto-lint proto-go

# generally not necessary unless we change library versions, but this DOES impact codegen
# formatting because it inherits that from the version of Go used to build tools.
clean:
	rm -rf $(BIN)
