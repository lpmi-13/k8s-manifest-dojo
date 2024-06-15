FROM golang:1.22.1-alpine3.19 as builder

WORKDIR /app

# this only uses the standard lib, so no need to download dependencies
COPY go.mod main.go ./

RUN CGO_ENABLED=0 go build -ldflags="-w -s" -o /load-generator

FROM scratch

COPY --from=builder /load-generator /load-generator

# starts the process passing in the argument for url and
# number of concurrent executions
CMD ["/load-generator", "http://localhost:3000", "10"]
