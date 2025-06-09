# main - Dockerfile for PINOperation
FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS runtime
WORKDIR /app

COPY --from=builder /app/node_modules ./node_modules
COPY . .

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

USER nextjs

EXPOSE 3000
ENV PORT 3000
ENV NODE_ENV production

CMD ["node", "index.js"]

# Code Update 1760517877-19414

# Additional Implementation 1760517877

# Additional Implementation 1760517877

# Additional Implementation 1760517877

# Code Update 1760517877-26928

# Additional Implementation 1760517877

# Additional Implementation 1760517878

# Code Update 1760517878-22796

# Code Update 1760517878-17647

# Additional Implementation 1760517878

# Code Update 1760517878-11953

# Additional Implementation 1760517878

# Code Update 1760517878-10891

# Additional Implementation 1760517878

# Additional Implementation 1760517879

# Code Update 1760517879-8426

# Additional Implementation 1760517879

# Code Update 1760517879-28871

# Code Update 1760517879-27001

# Additional Implementation 1760517879

# Code Update 1760517879-32020
