
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

1. **Package the Application:**
   - Zip your Django project files and dependencies.

2. **Upload to AWS Lambda:**
   - Follow AWS Lambda and API Gateway setup instructions to upload and configure your Django application.

3. **Configure Environment Variables:**
   - Set environment variables such as `DJANGO_SETTINGS_MODULE` and `DATABASE_URL` in the AWS Lambda console.

4. **Deploy the API:**
   - Use AWS API Gateway to expose your Lambda function as a web service.


