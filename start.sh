#!/bin/bash
python3 /Users/gyusik/wedding/server.py &

cloudflared tunnel --url http://localhost:8080 2>&1 | while read line; do
    if echo "$line" | grep -q "trycloudflare.com"; then
        url=$(echo "$line" | grep -o 'https://[^ ]*trycloudflare.com')
        echo ""
        echo "=============================="
        echo "청첩장 링크: ${url}/code/"
        echo "=============================="
        echo ""
    fi
done
