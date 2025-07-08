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

# Additional Implementation 1760517877

# Additional Implementation 1760517877

# Additional Implementation 1760517877

# Additional Implementation 1760517877

# Code Update 1760517877-3

# Code Update 1760517877-6631

# Code Update 1760517877-15766

# Additional Implementation 1760517877

# Additional Implementation 1760517878

# Additional Implementation 1760517878

# Code Update 1760517878-28225

# Additional Implementation 1760517878

# Additional Implementation 1760517878

# Code Update 1760517878-1469

# Code Update 1760517878-19908

# Additional Implementation 1760517878

# Code Update 1760517878-20761

# Additional Implementation 1760517878

# Additional Implementation 1760517878

# Code Update 1760517878-21894

# Additional Implementation 1760517878

# Code Update 1760517878-14881

# Code Update 1760517879-13353

# Additional Implementation 1760517879

# Additional Implementation 1760517879

# Additional Implementation 1760517879

# Code Update 1760517879-9202

# Additional Implementation 1760517879

# Code Update 1760517879-2543

# Code Update 1760517879-26242

# Code Update 1760517879-13716

# Additional Implementation 1760517879

# Additional Implementation 1760517879

# Additional Implementation 1760517879

# Additional Implementation 1760517879

# Code Update 1760517879-11073

# Code Update 1760517879-21959

# Additional Implementation 1760517879

# Code Update 1760517879-22545

# Additional Implementation 1760517880

# Additional Implementation 1760517880

# Additional Implementation 1760517880

# Additional Implementation 1760517880

# Code Update 1760517880-15456

# Additional Implementation 1760517880

# Additional Implementation 1760517880

# Additional Implementation 1760517880

# Code Update 1760517880-13634

# Code Update 1760517880-1563

# Code Update 1760517880-26762

# Additional Implementation 1760517880

# Code Update 1760517881-16998

# Additional Implementation 1760517881

# Code Update 1760517881-1493

# Additional Implementation 1760517881

# Additional Implementation 1760517881

# Additional Implementation 1760517881

# Additional Implementation 1760517881
