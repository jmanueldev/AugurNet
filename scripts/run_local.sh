#!/bin/bash
echo "Running AugurNet..."
uvicorn api.main:app --reload