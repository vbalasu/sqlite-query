export AWS_PROFILE=vbalasu_admin
export AWS_DEFAULT_REGION=us-east-1
chalice deploy

# Deploy to Nginx on the Cloudmatica server
scp -r dist cloudmatica:/usr/share/nginx/html/sqlite-query
