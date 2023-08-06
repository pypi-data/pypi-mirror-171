## Setup

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## Building .tar.gz

Run the following commands to generate a distributable source package:

```
python -m pip install --upgrade build
python -m build --dist
```

### Why not .whl?

This package uses gRPC to communicate with the Saleae Logic2 application. This depends on using protobuf (`protoc`) to generate python files from a .proto file. If the version of protobuf used to generate the python files differs from the grpcio or protobuf version installed on the client machine there may be compatibility issues.

In particular, there was a break @ protobuf 4.21.0, released on May 6, 2022: https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates

Instead of distributing .whl files with generated files from a specific protobuf version, we have instead decided to release a source distribution that will generate the necessary files at install time, using the installed protobuf version.

This isn't a perfect solution - if the protobuf package is updated after generating the files, it may become incompatible. This can be resolved by reinstalling logic2-automation via pip: `pip install --force-reinstall logic2-automation`. This requires a manual step, but we think this is a good compromise that still allows users on old versions to use this package.

## Changelog

### 1.0.2

- Update the distribution to only include a source distribution so that gRPC/protobuf files can be generated at install time, and be based on the installed version of grpcio/grpcio-tools/protobuf.

### 1.0.1

- YANKED!
  - This release was pulled shortly after it was released due to a conflict between the latest gRPC and the generated protobuf files.
- Change `grpc` & `grpc-tools` dependency to version `>=1.13.0`. This lowers the minimum version, and doesn't stick it to a specific version.

### 1.0.0

- First release
