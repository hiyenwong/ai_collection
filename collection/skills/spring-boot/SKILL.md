---
name: spring-boot
description: Spring Boot 框架开发指南，包含自动配置、Starters、Actuator、最佳实践
version: 3.x
tags: [java, spring, spring-boot, microservices, autoconfiguration, starters, actuator]
created: 2026-03-31
source: https://github.com/spring-projects/spring-boot
---

# Spring Boot 开发指南

## Activation Keywords

- Spring Boot
- Spring Boot 自动配置
- Spring Boot starter
- Spring Boot actuator
- Spring Boot 微服务
- Spring Boot REST API

## Overview

Spring Boot 帮助你以最少的配置创建生产级 Spring 应用。核心特性：
- **自动配置**：根据依赖自动配置 Spring 应用
- **Starters**：依赖描述符，简化构建配置
- **Actuator**：生产级监控和管理
- **嵌入式服务器**：内置 Tomcat/Jetty/Undertow
- **无 XML 配置**：纯 Java 配置

## Core Concepts

### 1. 自动配置 (Auto-Configuration)

Spring Boot 根据类路径下的依赖自动配置应用：

```java
@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

**@SpringBootApplication 包含：**
- `@Configuration` - 配置类
- `@EnableAutoConfiguration` - 启用自动配置
- `@ComponentScan` - 组件扫描

**条件注解：**
```java
@Configuration
@ConditionalOnClass(DataSource.class)
@ConditionalOnMissingBean(DataSource.class)
public class DataSourceAutoConfiguration {
    // 仅当类路径有 DataSource 且没有自定义 DataSource 时生效
}
```

### 2. Starters

常用 Starters：

| Starter | 用途 |
|---------|------|
| spring-boot-starter-web | Web 应用（RESTful、Spring MVC） |
| spring-boot-starter-data-jpa | JPA + Hibernate |
| spring-boot-starter-data-mongodb | MongoDB |
| spring-boot-starter-security | Spring Security |
| spring-boot-starter-test | 测试框架 |
| spring-boot-starter-actuator | 监控端点 |
| spring-boot-starter-validation | Bean Validation |

### 3. 配置管理

**application.yml:**
```yaml
server:
  port: 8080

spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
    username: root
    password: secret
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true

management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics
```

**Profile 配置:**
```yaml
# application-dev.yml
spring:
  profiles: dev
server:
  port: 8081

# application-prod.yml
spring:
  profiles: prod
server:
  port: 80
```

## Quick Start

### 创建项目

**方式 1：Spring Initializr**
```bash
# 使用 Spring Initializr
https://start.spring.io/

# 或使用 curl
curl https://start.spring.io/starter.zip \
  -d dependencies=web,data-jpa,h2 \
  -d type=maven-project \
  -d language=java \
  -d bootVersion=3.2.0 \
  -o myproject.zip
```

**方式 2：Spring Boot CLI**
```bash
# 安装 (macOS)
brew install springboot

# 创建项目
spring init --dependencies=web,data-jpa myproject
```

**方式 3：Maven/Gradle**

Maven pom.xml:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.2.0</version>
</parent>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>

<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

### REST API 示例

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping
    public List<User> getAllUsers() {
        return userService.findAll();
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        return userService.findById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public User createUser(@Valid @RequestBody User user) {
        return userService.save(user);
    }
    
    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        user.setId(id);
        return userService.save(user);
    }
    
    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteUser(@PathVariable Long id) {
        userService.deleteById(id);
    }
}
```

### JPA 实体

```java
@Entity
@Table(name = "users")
public class User {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @NotBlank
    @Column(nullable = false)
    private String name;
    
    @Email
    @Column(unique = true, nullable = false)
    private String email;
    
    @CreationTimestamp
    private LocalDateTime createdAt;
    
    @UpdateTimestamp
    private LocalDateTime updatedAt;
    
    // getters, setters
}

public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    
    @Query("SELECT u FROM User u WHERE u.name LIKE %:name%")
    List<User> findByNameContaining(@Param("name") String name);
}
```

## Actuator 监控

### 启用端点

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus,env,beans
  endpoint:
    health:
      show-details: always
```

### 常用端点

| 端点 | 描述 |
|------|------|
| /actuator/health | 健康检查 |
| /actuator/info | 应用信息 |
| /actuator/metrics | 指标数据 |
| /actuator/env | 环境变量 |
| /actuator/beans | Spring Beans |
| /actuator/mappings | URL 映射 |

### 自定义健康检查

```java
@Component
public class CustomHealthIndicator implements HealthIndicator {
    
    @Override
    public Health health() {
        // 自定义健康检查逻辑
        boolean healthy = checkExternalService();
        
        if (healthy) {
            return Health.up()
                .withDetail("service", "external-api")
                .withDetail("status", "available")
                .build();
        } else {
            return Health.down()
                .withDetail("service", "external-api")
                .withDetail("error", "connection failed")
                .build();
        }
    }
}
```

## 最佳实践

### 1. 项目结构

```
src/main/java/
└── com/example/myapp/
    ├── MyApplication.java
    ├── config/           # 配置类
    │   ├── SecurityConfig.java
    │   └── WebConfig.java
    ├── controller/       # REST 控制器
    │   └── UserController.java
    ├── service/          # 业务逻辑
    │   ├── UserService.java
    │   └── impl/
    │       └── UserServiceImpl.java
    ├── repository/       # 数据访问
    │   └── UserRepository.java
    ├── entity/           # JPA 实体
    │   └── User.java
    ├── dto/              # 数据传输对象
    │   └── UserDTO.java
    └── exception/        # 异常处理
        └── GlobalExceptionHandler.java
```

### 2. 全局异常处理

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.NOT_FOUND.value(),
            ex.getMessage(),
            LocalDateTime.now()
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidation(MethodArgumentNotValidException ex) {
        List<String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .map(e -> e.getField() + ": " + e.getDefaultMessage())
            .collect(Collectors.toList());
        
        ErrorResponse error = new ErrorResponse(
            HttpStatus.BAD_REQUEST.value(),
            "Validation failed",
            errors,
            LocalDateTime.now()
        );
        return ResponseEntity.badRequest().body(error);
    }
}
```

### 3. 配置属性

```java
@ConfigurationProperties(prefix = "app")
@Component
public class AppConfig {
    private String name;
    private int timeout;
    private List<String> allowedOrigins;
    
    // getters, setters
}
```

```yaml
app:
  name: My Application
  timeout: 30000
  allowed-origins:
    - https://example.com
    - https://api.example.com
```

### 4. 测试

```java
@SpringBootTest
@AutoConfigureMockMvc
class UserControllerTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    void shouldReturnUser() throws Exception {
        User user = new User(1L, "John", "john@example.com");
        when(userService.findById(1L)).thenReturn(Optional.of(user));
        
        mockMvc.perform(get("/api/users/1"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.name").value("John"))
            .andExpect(jsonPath("$.email").value("john@example.com"));
    }
}
```

## Spring Boot 3 新特性

### 1. Java 17+ 要求

Spring Boot 3 需要 Java 17 或更高版本。

### 2. Jakarta EE

从 `javax.*` 迁移到 `jakarta.*`：
```java
// 旧版本
import javax.servlet.http.HttpServletRequest;
import javax.persistence.Entity;

// Spring Boot 3
import jakarta.servlet.http.HttpServletRequest;
import jakarta.persistence.Entity;
```

### 3. 原生编译支持

使用 GraalVM 进行原生编译：
```bash
./mvnw native:compile -Pnative
```

### 4. 可观测性改进

```yaml
management:
  tracing:
    enabled: true
    sampling:
      probability: 1.0
  otlp:
    tracing:
      endpoint: http://localhost:4318/v1/traces
```

## 常用命令

```bash
# 运行应用
./mvnw spring-boot:run

# 打包
./mvnw clean package

# 运行 JAR
java -jar target/myapp-0.0.1-SNAPSHOT.jar

# 查看自动配置报告
java -jar myapp.jar --debug

# Actuator 端点
curl http://localhost:8080/actuator/health
curl http://localhost:8080/actuator/metrics
```

## Tools Used

- `exec` - 运行 Maven/Gradle 命令
- `write` - 创建配置文件和代码
- `read` - 读取现有项目文件
- `web_fetch` - 获取 Spring Boot 文档

## References

- 官方文档: https://docs.spring.io/spring-boot/
- GitHub: https://github.com/spring-projects/spring-boot
- Spring Initializr: https://start.spring.io/

## Related Skills

- fullstack-engineer (Java Web 开发)
- security-engineer (Spring Security 配置)