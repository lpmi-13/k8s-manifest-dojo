FROM golang:1.22.1-alpine3.19 as builder

WORKDIR /app

COPY go.mod ./

WORKDIR /app

COPY main.go ./

RUN CGO_ENABLED=0 go build -ldflags="-w -s" -o /load-generator

FROM scratch

COPY --from=builder /load-generator /load-generator

# starts the process passing in the argument for url and
# number of concurrent executions
CMD ["/load-generator", "http://localhost:3000", "10"]