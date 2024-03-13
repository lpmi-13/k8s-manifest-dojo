FROM golang:1.22.1-alpine3.19

WORKDIR /app

COPY go.mod ./

WORKDIR /app

COPY main.go ./

RUN CGO_ENABLED=0 go build -ldflags="-w -s" -o /load-generator

# starts the process passing in the argument for url and
# number of concurrent executions
CMD ["/load-generator", "http://localhost:3000", "10"]