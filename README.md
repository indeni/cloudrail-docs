# Cloudrail Docs
Documentation and tutorials for Cloudrail.

## Development
For local development, first clone this repository:

```bash
git clone https://github.com/indeni/cloudrail-docs
```

Next, descend into the repository and run the make install command - this will install docsify globally to your machine.
```bash
cd cloudrail-docs
make install
```

To build dynamically generated docs, run the following command:
```bash
make build
```

Finally, run the make run command to serve the docs on localhost:3000. Make any changes to markdown files as necessary, except auto-generated documentation (the rules directory).

```bash
make run
```
