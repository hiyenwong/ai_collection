# Docker Compose Templates

## Development Stack

### Full Stack Web App

```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - API_URL=http://api:8000
    depends_on:
      - api

  api:
    build: ./api
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=app
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

### ML/AI Stack

```yaml
version: '3.8'

services:
  jupyter:
    image: jupyter/tensorflow-notebook:latest
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
      - ./data:/home/jovyan/data
    environment:
      - JUPYTER_TOKEN=your-token

  mlflow:
    image: ghcr.io/mlflow/mlflow:v2.9.0
    ports:
      - "5000:5000"
    environment:
      - MLFLOW_BACKEND_STORE_URI=postgresql://user:pass@db:5432/mlflow
      - MLFLOW_ARTIFACT_ROOT=/mlflow/artifacts
    volumes:
      - mlflow_artifacts:/mlflow/artifacts
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mlflow
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  mlflow_artifacts:
  postgres_data:
```

### Monitoring Stack

```yaml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana
    depends_on:
      - prometheus

  alertmanager:
    image: prom/alertmanager:latest
    ports:
      - "9093:9093"
    volumes:
      - ./alertmanager.yml:/etc/alertmanager/alertmanager.yml:ro

volumes:
  prometheus_data:
  grafana_data:
```

## Database Templates

### PostgreSQL

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=${POSTGRES_USER:-user}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-pass}
      - POSTGRES_DB=${POSTGRES_DB:-app}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-user}"]
      interval: 10s
      timeout: 5s
      retries: 5

  pgadmin:
    image: dpage/pgadmin4:latest
    ports:
      - "5050:80"
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=admin
    depends_on:
      - postgres

volumes:
  postgres_data:
```

### MongoDB

```yaml
version: '3.8'

services:
  mongo:
    image: mongo:7
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=pass
    volumes:
      - mongo_data:/data/db

  mongo-express:
    image: mongo-express:latest
    ports:
      - "8081:8081"
    environment:
      - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
      - ME_CONFIG_MONGODB_ADMINPASSWORD=pass
      - ME_CONFIG_MONGODB_URL=mongodb://admin:pass@mongo:27017/
    depends_on:
      - mongo

volumes:
  mongo_data:
```

## Message Queue Templates

### RabbitMQ

```yaml
version: '3.8'

services:
  rabbitmq:
    image: rabbitmq:3-management-alpine
    ports:
      - "5672:5672"   # AMQP
      - "15672:15672" # Management UI
    environment:
      - RABBITMQ_DEFAULT_USER=admin
      - RABBITMQ_DEFAULT_PASS=admin
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq

volumes:
  rabbitmq_data:
```

### Kafka

```yaml
version: '3.8'

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      - ZOOKEEPER_CLIENT_PORT=2181
    volumes:
      - zookeeper_data:/var/lib/zookeeper/data

  kafka:
    image: confluentinc/cp-kafka:latest
    ports:
      - "9092:9092"
    environment:
      - KAFKA_BROKER_ID=1
      - KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
      - KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092
      - KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1
    volumes:
      - kafka_data:/var/lib/kafka/data
    depends_on:
      - zookeeper

  kafka-ui:
    image: provectuslabs/kafka-ui:latest
    ports:
      - "8080:8080"
    environment:
      - KAFKA_CLUSTERS_0_NAME=local
      - KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=kafka:9092
    depends_on:
      - kafka

volumes:
  zookeeper_data:
  kafka_data:
```