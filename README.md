# 🎓 Ram Sir Course Platform - Complete Setup Guide
### By Ramgopal Prajapati | Indore, M.P.

---

## 📋 Project Structure

```
ramsir_platform/
├── manage.py
├── requirements.txt
├── db.sqlite3               (auto-created)
├── ramsir_platform/
│   ├── settings.py
│   └── urls.py
├── courses/                 ← Main App
│   ├── models.py            ← All DB models
│   ├── views.py             ← All views/logic
│   ├── admin.py             ← Admin panel config
│   ├── forms.py             ← Django forms
│   ├── templatetags/
│   │   └── course_extras.py ← Custom filters
│   └── management/commands/
│       └── populate_courses.py ← Initial data
├── templates/               ← All HTML templates
│   ├── base.html            ← Base template with navbar/footer
│   ├── home.html            ← Homepage
│   ├── about.html           ← About Ram Sir page
│   ├── accounts/
│   │   └── register.html
│   ├── registration/
│   │   └── login.html
│   ├── courses/
│   │   ├── course_list.html
│   │   ├── course_detail.html
│   │   ├── module_detail.html  ← Learning page
│   │   └── payment.html
│   ├── dashboard/
│   │   ├── dashboard.html
│   │   ├── profile.html
│   │   ├── my_courses.html
│   │   ├── progress.html
│   │   └── history.html
│   └── events/
│       └── events.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── media/                   ← Uploaded files (auto-created)
```

---

## 🚀 INSTALLATION STEPS

### Step 1: Install Python & pip
```bash
python --version   # Should be 3.8+
```

### Step 2: Create Virtual Environment
```bash
cd ramsir_platform
python -m venv venv

# Activate:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Apply Database Migrations
```bash
python manage.py makemigrations courses
python manage.py migrate
```

### Step 5: Populate Initial Courses (15+ courses!)
```bash
python manage.py populate_courses
```

### Step 6: Create Admin Account
```bash
python manage.py createsuperuser
# Enter: username, email, password
```

### Step 7: Run the Server
```bash
python manage.py runserver
```

### Step 8: Open in Browser
```
http://127.0.0.1:8000/          ← Main website
http://127.0.0.1:8000/admin/    ← Admin panel
```

---

## 🔧 ADMIN PANEL GUIDE

### How to Add/Edit Courses:
1. Go to `http://127.0.0.1:8000/admin/`
2. Login with superuser credentials
3. Click **Courses** → **Add Course**
4. Fill: Title, Category, Type (Free/Paid), Price, Description
5. Scroll down → **Modules** section
6. Add modules with YouTube URL, text content, images

### How to Add YouTube Video to a Module:
1. Admin → Courses → Select a course
2. In Modules section → Add module
3. Set Content Type = "YouTube Video"
4. Paste YouTube URL (any format works):
   - `https://www.youtube.com/watch?v=XXXXXXXX`
   - `https://youtu.be/XXXXXXXX`
   - Just the video ID: `XXXXXXXX`
5. Save → Video auto-embeds on the website!

### How to Add Events:
1. Admin → Events → Add Event
2. Fill: Title, Description, Date, Type
3. Add image URL or upload image
4. Paste Google Form URL in "Registration Link"
5. Students click "Register" → Google Form opens!

### How to Verify Payments:
1. Admin → Payments → Find pending payment
2. Check transaction ID and screenshot
3. Change Status to "Completed" → Save
4. Student gets automatic course access!

### How to Add Free Text Content:
In Module text content field, use HTML:
```html
<h2>Topic Title</h2>
<p>Your explanation here...</p>
<pre><code>
# Python code example
print("Hello World!")
</code></pre>
<table border="1">
  <tr><th>Column 1</th><th>Column 2</th></tr>
  <tr><td>Data 1</td><td>Data 2</td></tr>
</table>
```

---

## 🤖 AI CONTENT GENERATION (Claude API)

### Setup Claude API:
1. Go to `https://console.anthropic.com`
2. Create account (free tier available)
3. Generate API key
4. Open `ramsir_platform/settings.py`
5. Replace: `CLAUDE_API_KEY = 'your-claude-api-key-here'`

### Use AI to Generate Module Content:
Make a POST request to `/api/ai-content/` (admin only):
```javascript
fetch('/api/ai-content/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken},
    body: JSON.stringify({
        topic: 'Python Decorators',
        content_type: 'detailed explanation with examples'
    })
})
.then(r => r.json())
.then(data => console.log(data.content))
```

Or use free AI tools to generate content and paste into admin:
- **ChatGPT** (chat.openai.com) - Free
- **Claude** (claude.ai) - Free tier
- **Gemini** (gemini.google.com) - Free

### Prompt to Use for Content Generation:
```
You are Ram Sir, a technical trainer from Indore India.
Create a detailed module about [TOPIC] for [COURSE NAME].
Format with HTML tags: <h2>, <h3>, <p>, <pre><code>, <ul>, <table>.
Include: explanation, code examples, diagrams description, practice tasks.
Make it beginner-friendly with real-world examples.
```

---

## 💳 PAYMENT SYSTEM

The platform uses a **manual UPI payment system** (no payment API needed!):

1. Student clicks "Buy Now" on paid course
2. Student sees your UPI ID and phone number
3. Student pays via PhonePe/GPay/Paytm
4. Student submits transaction ID + screenshot
5. **You verify in admin** → Student gets instant access

### To Update Your UPI Details:
Open `courses/views.py`, find `payment_page` function:
```python
context = {
    'upi_id': 'your-actual-upi@upi',    # Change this
    'phone': '9753528324',               # Change if needed
}
```

---

## 📱 FEATURES SUMMARY

### For Students:
- ✅ Register & Login free
- ✅ Browse 15+ free courses
- ✅ Enroll in free courses instantly
- ✅ Watch YouTube videos embedded
- ✅ Read rich text content with code
- ✅ Track module progress
- ✅ Buy premium courses via UPI
- ✅ Personal dashboard
- ✅ My Courses, Progress, History
- ✅ Edit profile with photo
- ✅ Register for events via Google Form

### For Admin (Ram Sir):
- ✅ Add/Edit/Delete courses
- ✅ Add YouTube videos to modules
- ✅ Add text, images, mixed content
- ✅ Manage free & paid courses
- ✅ Verify payments manually
- ✅ Add events with Google Form links
- ✅ See all students and enrollments
- ✅ Manage reviews

---

## 🌐 DEPLOYMENT (Make it Live)

### Option 1: Railway.app (Free)
1. Install Railway CLI
2. `railway init` → `railway up`
3. Set environment variables

### Option 2: PythonAnywhere (Free)
1. Create account at pythonanywhere.com
2. Upload files, setup virtualenv
3. Configure WSGI

### Option 3: Render.com (Free)
1. Connect GitHub repo
2. Set build command: `pip install -r requirements.txt && python manage.py migrate`
3. Set start command: `gunicorn ramsir_platform.wsgi`

---

## 📧 Contact
- **Ramgopal Prajapati (Ram Sir)**
- Email: ramsirdevix@gmail.com
- Phone: +91 9753528324
- Location: Vijay Nagar, Indore, M.P.
- Portfolio: https://ramgopal-prajapati.github.io/Ramgopal/
