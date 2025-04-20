# 🖼️ Auto Image Resizer (AWS Serverless Portfolio Project)

This project automatically resizes images uploaded to an S3 bucket and displays them in a responsive Bootstrap gallery. Built with fully serverless AWS services, it's a complete end-to-end cloud-native solution — perfect for production or portfolio use.

---

## 🚀 Features

- Upload images to the `original/` folder in S3
- Automatically resize images using AWS Lambda + Pillow
- Save resized versions in the `thumbnails/` folder (same S3 bucket)
- Store metadata (filename, timestamp, S3 URL) in DynamoDB
- Expose `/images` API using API Gateway
- Dynamically display images in a responsive gallery (HTML + Bootstrap)
- Host the gallery as a static website using Amazon S3

---

## 🧱 Architecture

Architecture Diagram ![ArchitectureDiagram](https://github.com/user-attachments/assets/bb45567f-1741-4125-953a-bfa21fb8992a)


---

## 🧰 Tech Stack

| Layer        | Service              |
|--------------|----------------------|
| Storage      | Amazon S3            |
| Compute      | AWS Lambda (Python)  |
| Image Library| Pillow (Python)      |
| Database     | Amazon DynamoDB      |
| API Layer    | Amazon API Gateway   |
| Frontend     | HTML + Bootstrap (S3 static site hosting) |

---

## 📂 Project Structure

auto-image-resizer/ ├── lambda/ # AWS Lambda image resizing function │ └── lambda_function.py ├── gallery/ # Frontend gallery (HTML, Bootstrap, JS) │ └── index.html ├── assets/ # Architecture diagram, screenshots, etc. │ └── architecture.png └── README.md # Project documentation

---

## 🛠️ How It Works

1. 📤 A user uploads an image to `original/` in S3.
2. ⚡ Lambda is triggered automatically via S3 event.
3. 🖼️ Lambda resizes the image to thumbnail size (128x128).
4. 📦 The resized image is saved to the `thumbnails/` folder.
5. 📝 Lambda logs image metadata to the DynamoDB table `ImageMetadata`.
6. 🌐 API Gateway exposes a REST endpoint `/images` to fetch all metadata.
7. 🌍 HTML + Bootstrap gallery calls the API and renders the thumbnails live.

---

## 🔧 Getting Started (Manual Deployment)

### 1. Set Up S3 Buckets
- Create a bucket: `auto-image-resizer-YOURNAME`
- Inside it, create two folders:
  - `original/` (for uploads)
  - `thumbnails/` (resized output)
- Make `thumbnails/` public (or use API Gateway to serve)

### 2. Create DynamoDB Table
- Table name: `ImageMetadata`
- Partition key: `filename` (String)

### 3. Deploy Lambda
- Runtime: Python 3.9
- Create Lambda triggered by uploads to `original/`
- Add permissions to access S3 + DynamoDB
- Install Pillow and include it in a deployment ZIP

### 4. Create REST API with API Gateway
- Resource: `/images`
- Method: `GET` → Connect to a Lambda that scans the DynamoDB table

### 5. Host the HTML Gallery
- Create a new S3 bucket (e.g., `auto-image-gallery-YOURNAME`)
- Upload `index.html`
- Enable static website hosting
- Point your HTML to use:
  ```js
  const apiUrl = "https://your-api-id.execute-api.us-east-2.amazonaws.com/prod/images";

---

## 📸 Example Output

Output 

![FetchData](https://github.com/user-attachments/assets/d742e7c3-190b-4a20-9c29-a2255d2bfbe8)





