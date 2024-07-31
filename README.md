
## Project Overview

### **Project Name**
This is the project i chose to work with
https://github.com/NowshadRuhan/Django-basic-project

### **Description**

This is a basic Django project for a music management application that allows users to manage and display information about musicians and their albums.

## Modifications Made

### **1. Added Artist Image Field**

**Modification:**
- Added a new field to the `Musician` model to display an artist's image.

**Details:**
- **Model Changes:**
  - Updated the `Musician` model to include an `ImageField` for storing artist images.
  - The `image` field stores the URL of the artist’s image in the database.

  ```python
 @deconstructible
class DefaultImageStorage(FileSystemStorage):
    def _save(self, name, content):
        if content.size == 0:
            # Use default image if no image is provided
            default_image_path = os.path.join(settings.MEDIA_ROOT, 'default_musician.jpg')
            with open(default_image_path, 'rb') as f:
                content = ContentFile(f.read())
        return super()._save(name, content)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    image = models.ImageField(upload_to='musicians/', storage=DefaultImageStorage(), blank=True)
  ```

- **Template Changes:**
  - Modified the template files to display the artist's image alongside their information.
  - Ensured that the image is displayed in a well-formatted manner within the project’s UI.

  
### **2. Template Improvements**

**Modification:**
- Made changes to the project’s templates to improve the overall appearance and user experience.

**Details:**
- **CSS and Layout Adjustments:**
  - Updated CSS files to enhance styling.
  - Adjusted layout and design elements to create a more appealing user interface.

### **3. Spelling Corrections**

**Modification:**
- Corrected spelling mistakes in the project’s content and templates.

**Details:**
- **Corrections Made:**
  - Reviewed and corrected spelling errors in text content.
  - Ensured that all textual elements are accurate and professional.

## How to Run the Application Locally

### **Prerequisites**

- Python 3.x
- Django
- Other dependencies listed in `requirements.txt`

### **Setup Instructions**

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

5. **Access the Application:**
   - Open a web browser and navigate to `http://127.0.0.1:8000/` to view the application.

## How to Deploy to AWS Lambda

### **Deployment Instructions**

### 1. **Prepare Your Django Application**

Before deploying your Django application to AWS Lambda, ensure it's ready for serverless deployment:

- **Remove Static Files:** Remove any static files from your application, as Lambda has limited storage.
- **Use Environment Variables:** Store sensitive data like database credentials in environment variables.
- **Update Settings:** Configure your Django settings to work with serverless environments, such as using `django-s3-storage` for static files.

### 2. **Set Up a Virtual Environment**

Create a virtual environment for your project and install all necessary dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. **Package Your Application**

Use a tool like **Zappa** to package and deploy your Django application to AWS Lambda. Install Zappa if you haven't already:

```bash
pip install zappa
```

### 4. **Configure Zappa**

Initialize Zappa in your Django project directory:

```bash
zappa init
```

### 5. **Deploy Your Application**

Deploy your application using Zappa:

```bash
zappa deploy production
```

This command packages your Django application and uploads it to AWS Lambda. Zappa will also create an API Gateway endpoint for your application.

### 6. **Set Environment Variables**

Set environment variables in AWS Lambda, including `DJANGO_SETTINGS_MODULE` and any other necessary settings. You can do this in the AWS Lambda console:

1. Go to the AWS Lambda console.
2. Select your function.
3. Under the "Configuration" tab, choose "Environment variables."
4. Add the required variables, such as:

   - `DJANGO_SETTINGS_MODULE`: Your settings module (e.g., `myproject.settings`).
   - `DATABASE_URL`: Your database connection string.

### 7. **Update Static and Media Files Handling**

Since AWS Lambda doesn't support persistent file storage, you'll need to use a service like Amazon S3 for static and media files. Update your `settings.py`:

```python
STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage'
DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'
AWS_S3_BUCKET_NAME = 'your-s3-bucket-name'
```

### 8. **Migrate the Database**

To run Django's database migrations on Lambda, use Zappa:

```bash
zappa manage production migrate
```

### 9. **Deploy API with AWS API Gateway**

AWS API Gateway will automatically be set up with Zappa. If you want to customize API Gateway further:

1. Go to the API Gateway console.
2. Select the API created by Zappa.
3. Customize routes, methods, and settings as needed.

### 10. **Testing and Maintenance**

- **Test Your Application:** After deployment, thoroughly test your application to ensure it functions correctly in the AWS Lambda environment.
- **Update and Redeploy:** For updates, use `zappa update production` to redeploy your changes.
- **Monitoring and Logs:** Use AWS CloudWatch for monitoring and logging. Check the Lambda and API Gateway dashboards for performance and error logs.

### Additional Resources

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/index.html)
- [AWS API Gateway Documentation](https://docs.aws.amazon.com/apigateway/index.html)
- [Zappa Documentation](https://github.com/Miserlou/Zappa)

