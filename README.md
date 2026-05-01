# 🤖 Binance Futures Trading Bot

A production-ready Python trading bot for Binance Futures Demo Trading platform with comprehensive validation, logging, and error handling.

## 📋 Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [Examples](#examples)
- [Logging](#logging)
- [Project Structure](#project-structure)
- [Error Handling](#error-handling)
- [Troubleshooting](#troubleshooting)
- [Submission Requirements](#submission-requirements)

## ✨ Features

- ✅ **Market Orders** - Instant execution at current market price
- ✅ **Limit Orders** - Execute only at specified price
- ✅ **Both Sides** - Support for BUY and SELL orders
- ✅ **Input Validation** - Comprehensive validation for all parameters
- ✅ **Error Handling** - Robust handling of API errors and network issues
- ✅ **Detailed Logging** - Complete logs of all API requests and responses
- ✅ **CLI Interface** - Both command-line and interactive modes
- ✅ **Order History** - Track all orders in current session
- ✅ **Account Info** - View balance and position information

## 📦 Prerequisites

- **Python 3.8+** (Tested with Python 3.13)
- **Binance Demo Trading Account** (Free)
- **Internet Connection** (for API calls)

## 🚀 Setup Instructions

### Step 1: Clone or Create Project Structure

```bash
# Create project directory
mkdir trading_bot
cd trading_bot

# Create required folders
mkdir bot
mkdir logs
