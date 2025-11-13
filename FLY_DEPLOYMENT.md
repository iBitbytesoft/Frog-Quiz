# Fly.io Deployment Guide for Frog Quiz App

## Prerequisites
1. Install flyctl: https://fly.io/docs/hands-on/install-flyctl/
2. Sign up/login to Fly.io: `flyctl auth signup` or `flyctl auth login`

## Deployment Steps

### 1. Initialize Fly.io App
```bash
# Launch the app (this will use fly.toml configuration)
flyctl launch --no-deploy

# Or if you want to create it manually:
flyctl apps create frog-quiz
```

### 2. Set Secrets (if needed)
```bash
# Example: if you have any API keys or secrets
flyctl secrets set SECRET_KEY=your-secret-key
```

### 3. Deploy the Application
```bash
# Deploy using the Dockerfile
flyctl deploy --dockerfile Dockerfile.flyio

# Or if using fly.toml default:
flyctl deploy
```

### 4. Check Status
```bash
# View app status
flyctl status

# View logs
flyctl logs

# Open in browser
flyctl open
```

## Configuration Details

### fly.toml
- **app**: "frog-quiz" (change to your preferred app name)
- **region**: "syd" (Sydney - change to nearest region: ord, lhr, sin, etc.)
- **port**: 8080 (matches main_web.py)
- **memory**: 256MB (increase if needed)
- **auto_stop/start**: Enabled for cost savings

### Dockerfile.flyio
- Uses Python 3.13 slim image
- Installs dependencies from requirements.txt
- Runs main_web.py on port 8080

## Useful Commands

```bash
# Scale to multiple machines
flyctl scale count 2

# Increase memory
flyctl scale memory 512

# View app details
flyctl info

# SSH into machine
flyctl ssh console

# View metrics
flyctl dashboard

# Restart app
flyctl apps restart

# Delete app
flyctl apps destroy frog-quiz
```

## Troubleshooting

### App won't start
```bash
flyctl logs
```

### Port issues
Make sure main_web.py runs on port 8080 or update fly.toml

### Out of memory
```bash
flyctl scale memory 512
```

### Slow performance
```bash
flyctl scale vm shared-cpu-2x
```

## Cost Optimization
- Free tier: 3 shared-cpu-1x 256MB VMs
- auto_stop_machines: Stops when idle
- auto_start_machines: Starts on request
- min_machines_running: 0 (only runs when accessed)

## Custom Domain (Optional)
```bash
flyctl certs create yourdomain.com
flyctl certs show yourdomain.com
```

Then add DNS records as shown in the output.
