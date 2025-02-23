FROM maven:3.8.4-openjdk-11 AS build
WORKDIR /app
COPY backend/pom.xml .  # Copy the pom.xml file
COPY backend/src ./src  # Copy the source code
RUN mvn clean package

FROM openjdk:11-jre-slim
WORKDIR /app
COPY --from=build /app/target/backend-1.0.0.jar .
CMD ["java", "-jar", "backend-1.0.0.jar"]