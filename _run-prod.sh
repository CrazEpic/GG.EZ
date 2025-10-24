#!/bin/bash
echo "Cleaning processes"
(npx pm2 delete all)
echo "Building and starting web server"
(npm run build; npx pm2 start ecosystem.config.cjs --only Nuxt-Web-Server)
echo "Starting FastAPI server"
(npx pm2 start ecosystem.config.cjs --only FastAPI-Backend)