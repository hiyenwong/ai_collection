#!/bin/bash
# Docker helper functions

# Quick container cleanup
docker_cleanup() {
    echo "Cleaning up Docker resources..."
    docker container prune -f
    docker image prune -f
    docker volume prune -f
    docker network prune -f
    echo "Done!"
}

# Show container stats
docker_stats() {
    docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"
}

# Find container by port
docker_find_by_port() {
    local port=$1
    docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" | grep ":$port"
}

# Quick exec into container
docker_sh() {
    local container=$1
    docker exec -it "$container" /bin/sh
}

# Quick bash into container
docker_bash() {
    local container=$1
    docker exec -it "$container" /bin/bash
}

# Show container environment
docker_env() {
    local container=$1
    docker inspect "$container" --format='{{range .Config.Env}}{{println .}}{{end}}'
}

# Show container IP
docker_ip() {
    local container=$1
    docker inspect "$container" --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
}

# Export container logs with timestamp
docker_export_logs() {
    local container=$1
    local output="${2:-${container}_$(date +%Y%m%d_%H%M%S).log}"
    docker logs "$container" > "$output" 2>&1
    echo "Logs exported to: $output"
}

# List all container ports
docker_ports() {
    docker ps --format "table {{.Names}}\t{{.Ports}}"
}

# Show disk usage summary
docker_disk() {
    echo "=== Docker Disk Usage ==="
    docker system df
    echo ""
    echo "=== Top 5 Large Images ==="
    docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}" | head -6
    echo ""
    echo "=== Top 5 Large Volumes ==="
    docker volume ls -q | while read vol; do
        echo "$vol: $(docker run --rm -v "$vol:/data" alpine du -sh /data 2>/dev/null | cut -f1)"
    done | sort -hr | head -5
}

# Quick build and run
docker_quick_run() {
    local name=$1
    local port=$2
    shift 2
    docker build -t "$name" . && docker run -d --name "$name" -p "$port" "$name" "$@"
}

# Stop all containers
docker_stop_all() {
    docker stop $(docker ps -q)
}

# Remove all stopped containers
docker_rm_stopped() {
    docker rm $(docker ps -aq -f status=exited)
}

# Follow logs with highlight
docker_logs_color() {
    local container=$1
    docker logs -f "$container" 2>&1 | grep --color=always -E "ERROR|WARN|INFO|DEBUG|^"
}

# Create a backup of a volume
docker_volume_backup() {
    local volume=$1
    local output="${2:-${volume}_backup_$(date +%Y%m%d_%H%M%S).tar.gz"
    docker run --rm -v "$volume:/data" -v "$(pwd):/backup" alpine tar czf "/backup/$output" /data
    echo "Volume backed up to: $output"
}

# Restore volume from backup
docker_volume_restore() {
    local volume=$1
    local backup=$2
    docker volume create "$volume" 2>/dev/null || true
    docker run --rm -v "$volume:/data" -v "$(pwd):/backup" alpine sh -c "cd / && tar xzf /backup/$backup"
    echo "Volume restored from: $backup"
}