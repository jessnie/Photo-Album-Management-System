# 📸 Quick Start Guide - Photo Album Manager

## Getting Started in 5 Minutes

### Step 1: Access the Application
- Go to `https://your-app.onrender.com` (or your local development server)
- You'll see the home page with navigation

### Step 2: Create an Account
1. Click **Register** in the top right
2. Fill in:
   - **Username**: Your unique username
   - **Email**: Your email address
   - **Password**: Strong password (6+ characters)
   - **Confirm Password**: Re-enter password
3. Click **Register**
4. You'll be redirected to login

### Step 3: Log In
1. Enter your username and password
2. Click **Login**
3. You're now authenticated and ready to upload!

---

## Main Features

### 📤 Uploading Photos

1. On the **Gallery** page, find the "Upload New Photo" form
2. Fill in:
   - **Title**: Name of your photo (e.g., "Mountain Sunset")
   - **Description**: Details about the photo (optional)
   - **Image**: Click to select an image file (JPG, PNG, WebP)
3. Click **Upload Photo**
4. Your photo will appear in the gallery! ✅

**Supported formats**: JPG, PNG, WebP (Max 100MB)

### 🔍 Browsing & Searching

1. **View all photos**: Scroll through the gallery
2. **Search**: Type in the search box to find photos by:
   - Title
   - Description
3. **Pagination**: Use page controls to view more photos

### ✏️ Editing Photos

**Only you or admins can edit your photos**

1. Find your photo in the gallery
2. Click the **Edit** button
3. Modify:
   - Title
   - Description
   - Image (replace with new image)
4. Click **Save Changes**

### 🗑️ Deleting Photos

**Only you or admins can delete your photos**

1. Click the **Delete** button on your photo
2. **Confirm** the deletion warning
3. Photo is permanently removed
4. Image is deleted from cloud storage

### 👤 Managing Your Profile

1. Click on your **Username** in the top navigation
2. View your profile information:
   - **Username** (read-only)
   - **Email** (editable)
   - **First Name** (editable)
   - **Last Name** (editable)
   - **Photo count** - How many photos you've uploaded
   - **Account status** - User or Admin
3. Update fields and click **Update Profile**

### 🎨 Viewing Your Photos

1. Click **My Photos** in navigation
2. See only photos you uploaded
3. Same edit/delete functionality as main gallery

---

## Important Information

### How RBAC Works

**Regular Users**:
- ✅ Create account
- ✅ Upload photos
- ✅ Edit own photos
- ✅ Delete own photos
- ✅ View all photos
- ✅ Search photos
- ❌ Delete others' photos
- ❌ Access admin panel

**Administrators**:
- ✅ Everything users can do, plus:
- ✅ Edit any photo
- ✅ Delete any photo
- ✅ Manage user accounts
- ✅ Access admin panel at `/admin/`
- ✅ View all user data

### Account Security

- 🔒 Passwords are encrypted (never stored in plain text)
- 🔒 Sessions expire automatically
- 🔒 CSRF protection enabled
- 🔒 All data encrypted in transit (HTTPS)

### Image Storage

- ☁️ Images stored on Cloudinary (secure cloud storage)
- ☁️ Not stored on server (scalable)
- ☁️ Automatically optimized for web (faster loading)
- ☁️ Backed up by Cloudinary

---

## Troubleshooting

### "Image upload failed"
- Check file is under 100MB
- Supported formats: JPG, PNG, WebP
- Try uploading a different image

### "You don't have permission"
- You can only edit/delete your own photos
- Ask an admin if you need to modify another's photo
- Or create a new account if needed

### "Page not loading"
- Check your internet connection
- Try refreshing the page (F5)
- Clear browser cache and try again
- Contact support if persists

### "Can't log in"
- Check username and password spelling
- Use "Register" if you haven't created account yet
- Reset password via email (if available)

### "Images look blurry"
- Upload high-quality images
- Cloudinary automatically optimizes
- Try uploading at high resolution

---

## Best Practices

### ✅ Do's
- Use descriptive titles and descriptions
- Upload high-quality images
- Keep passwords private and strong
- Log out on shared computers
- Report broken features to admins

### ❌ Don'ts
- Don't share your password
- Don't upload copyrighted images without permission
- Don't spam or upload inappropriate content
- Don't try to access other users' accounts
- Don't disable JavaScript (needed for features)

---

## Tips & Tricks

### Bulk Upload
1. Upload multiple photos one at a time
2. They automatically appear in gallery
3. Most recent uploads show first

### Organization
- Use meaningful titles (not "Photo 1", "Photo 2")
- Add descriptive text in description field
- Makes searching easier later

### Search Tips
- Search is case-insensitive
- Searches both title and description
- Use keywords that might appear in photos

### Mobile Friendly
- Website works on phones and tablets
- Touch-friendly buttons and forms
- Responsive design adapts to screen size

---

## Features Coming Soon

These features may be added in future updates:
- 💭 Comments on photos
- ❤️ Like/favorite photos
- 📤 Share photos with other users
- 📁 Organize photos into albums
- 📊 Photo statistics and analytics
- 🔗 Direct photo sharing links
- 📱 Mobile app

---

## Getting Help

### Contact Support
If you encounter issues:
1. Check this guide first
2. Try troubleshooting section above
3. Email: support@example.com
4. GitHub Issues: [Link to repository]

### Report Bugs
Found a bug? Help us fix it:
1. Note what went wrong
2. Write down steps to reproduce
3. Contact support with details
4. Include screenshots if possible

---

## Security & Privacy

### What data we collect
- Username and email (for account)
- Photos you upload
- Activity logs (for security)

### What we DON'T do
- Sell your data
- Share with third parties
- Use for marketing
- Track personal browsing

### Your rights
- ✅ Download your photos anytime
- ✅ Delete your account (loses photos)
- ✅ Update your information
- ✅ Privacy with your uploads

---

## FAQ

**Q: Can I download my photos?**
A: Yes! Click on any photo and download button appears.

**Q: How many photos can I upload?**
A: Unlimited! (Limited by storage quota)

**Q: Are my photos public?**
A: Yes, visible to anyone on the site. For private gallery, contact admin.

**Q: What if I forget my password?**
A: Contact an administrator for password reset.

**Q: Can I delete my account?**
A: Contact admin. Note: Your photos will also be deleted.

**Q: What formats do you support?**
A: JPG, PNG, WebP (up to 100MB each)

**Q: Is there a mobile app?**
A: Currently web-only. Mobile web app works on all devices.

**Q: How long are photos stored?**
A: Indefinitely until you delete them.

---

## Happy Uploading! 📸

Enjoy sharing your photos with the Photo Album Manager!

For more help, visit the full [README.md](README.md) or check out the [Deployment Guide](DEPLOYMENT.md).
