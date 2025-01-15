import pandas as pd

# Enhanced dataset for SOC team with realistic descriptions and additional fields
data = {
    'description': [
        'User input not sanitized before executing SQL query, enabling potential exfiltration of sensitive data using malicious payloads.',
        'JavaScript code injected via user input, bypassing input validation and resulting in reflected XSS attacks in the login form.',
        'Remote code execution possible due to stack-based buffer overflow in file upload handler, allowing system compromise.',
        'Cross-site scripting (XSS) vulnerability in user feedback form due to lack of output encoding, allowing session hijacking.',
        'Command injection via unvalidated parameters in admin panel script execution endpoint.',
        'Open redirect flaw in password recovery feature, leading users to a phishing website.',
        'Sensitive data exposure due to usage of deprecated DES encryption in the API token generation process.',
        'Web server misconfigured to expose `/admin/debug` endpoints to public access without authentication.',
        'Broken authentication vulnerability enabling brute force attacks on login due to lack of account lockout mechanisms.',
        'Insecure direct object references in file download service, exposing arbitrary files by manipulating the resource ID.',
        # Additional expanded variations
        'Admin portal vulnerable to unsanitized SQL commands through malformed login credentials.',
        'Attackers use DOM-based XSS exploiting unsanitized user query parameters on search pages.',
        'Poor password reset logic revealing secure tokens in email headers.',
        'Remote attackers upload oversized files causing stack overflow and unauthorized execution.',
        'Insecure usage of outdated cryptographic hash algorithms leaking sensitive data hashes.',
        'Brute force enabled due to lack of multifactor authentication in admin login pages.',
        'Input filtering bypass enables path traversal and read access to internal configuration files.',
        'Absence of anti-CSRF tokens in transaction forms allows unauthorized fund transfers.',
        'Sensitive data exposed in `/logs/debug` endpoint without proper authentication.',
        'Improper XML entity definitions expose server to XXE-based local data harvesting.',
        'Vulnerable JavaScript inclusion in user-facing widgets, facilitating malicious code execution.',
        'Session fixation flaw through reuse of prior session IDs post-user login.',
        'Open redirects exploit improper URL sanitization during email link creation.',
        'Poor implementation of clickjacking controls exposes financial transaction pages.',
        'Lack of proper file upload validation enables shell execution via disguised malicious images.',
    ],
    'category': [
        'SQL Injection',
        'XSS',
        'Remote Code Execution',
        'XSS',
        'Command Injection',
        'Open Redirect',
        'Sensitive Data Exposure',
        'Security Misconfiguration',
        'Broken Authentication',
        'Insecure Direct Object References',
        # Additional categories
        'SQL Injection',
        'XSS',
        'Sensitive Data Exposure',
        'Remote Code Execution',
        'Insecure Cryptographic Storage',
        'Broken Authentication',
        'Path Traversal',
        'Cross-Site Request Forgery (CSRF)',
        'Sensitive Data Exposure',
        'XML External Entity (XXE) Injection',
        'Remote Code Execution',
        'Session Fixation',
        'Open Redirect',
        'Clickjacking',
        'Insecure File Upload',
    ],
    'severity': [
        'High', 'Medium', 'Critical', 'Medium', 'High', 'Medium', 'High', 'Medium', 'High', 'High',
        # Additional severity levels
        'High',
        'Medium',
        'High',
        'Critical',
        'High',
        'High',
        'High',
        'Medium',
        'Medium',
        'Critical',
        'Critical',
        'Medium',
        'Medium',
        'High',
        'Critical',
    ]
}

# Verify lengths of all arrays in data
lengths = [len(v) for v in data.values()]
if len(set(lengths)) != 1:
    raise ValueError("All columns must have the same number of entries. Current lengths: " + str(lengths))

# Create a dataframe
df = pd.DataFrame(data)

# Show the first few records
print("First few rows of the dataset:")
print(df.head())

# Save to CSV
df.to_csv('advanced_vulnerability_dataset.csv', index=False)

print("Enhanced dataset created and saved as advanced_vulnerability_dataset.csv")
