# SFT with Unsloth on Lambda Cloud

This repository contains a simple Docker setup to fine tune
`unsloth/DeepSeek-R1-Distill-Qwen-7B` on a single H100 GPU.
The provided Dockerfile installs Unsloth with Flash Attention 3
and includes a sample DeepSpeed configuration (`ds_zero3_nvme.json`).

A helper script (`lambda_build.py`) demonstrates how to trigger a Docker
build using the Lambda Cloud API so the image can be used on an H100
instance. Edit the environment variables in the script to match your
Lambda project and credentials.
