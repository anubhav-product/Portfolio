# Adding Your Resume to the Portfolio

## Quick Steps

1. **Locate your resume file** on your Desktop (it should be a PDF file)

2. **Copy it to the portfolio folder**:
   ```bash
   cp ~/Desktop/your-resume-name.pdf /workspaces/Portfolio/static/downloads/resume.pdf
   ```

3. **Verify the file**:
   ```bash
   ls -lh /workspaces/Portfolio/static/downloads/
   ```

4. **Restart the Flask server** (if it's running):
   - Stop the current server (Ctrl+C in the terminal)
   - Run: `python app.py`

5. **Test the download**:
   - Open http://127.0.0.1:5000
   - Click the "Download Resume" button in the hero section
   - Your resume should download!

## Alternative: If you know your resume filename

If your resume is named something like `Anubhav_Resume.pdf`, run:
```bash
cp ~/Desktop/Anubhav_Resume.pdf /workspaces/Portfolio/static/downloads/resume.pdf
```

## What the portfolio expects

- File location: `/workspaces/Portfolio/static/downloads/resume.pdf`
- File format: PDF (recommended)
- The download button will automatically serve this file

## Troubleshooting

- **File not found**: Make sure your resume is actually on the Desktop
- **Button doesn't work**: Check browser console for errors
- **Wrong file downloads**: Verify the file path is correct

## Push to GitHub

After adding your resume, commit and push:
```bash
git add static/downloads/resume.pdf
git commit -m "Add resume for download"
git push origin main
```

---

**Note**: The portfolio is already configured to handle the resume download. You just need to copy your PDF file to the right location!
