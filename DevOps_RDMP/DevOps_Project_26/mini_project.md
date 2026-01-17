Project Overview

This demo project demonstrates how to securely launch an Ubuntu EC2 instance in AWS and connect to it using an RSA-based key pair. The project focuses on key pair management, SSH authentication, and basic troubleshooting—core skills expected from a DevOps engineer.
---

# Step-by-Step Demo: Launch Ubuntu EC2 and Connect Using Key Pair

---

## Step 1: Login to AWS Console

1. Open the AWS Management Console.
2. Sign in with your AWS credentials.
3. Navigate to **Amazon EC2**.

---

## Step 2: Create a Key Pair

1. In EC2 dashboard, click **Key Pairs** (under *Network & Security*).
2. Click **Create key pair**.
3. Enter the following:

   * **Key pair name:** `xfusion-kp`
   * **Key pair type:** RSA
   * **Private key format:** `.pem`
4. Click **Create key pair**.
5. The file **`xfusion-kp.pem`** is downloaded automatically.
6. Store the file securely.

---

## Step 3: Launch an Ubuntu EC2 Instance

1. In EC2 dashboard, click **Launch instance**.
2. Choose **Ubuntu Server (22.04 LTS)**.
3. Select instance type (e.g., `t2.micro`).
4. Under **Key pair**, select **`xfusion-kp`**.
5. Configure security group:

   * Allow **SSH (port 22)** from your IP.
6. Click **Launch instance**.

---

## Step 4: Get Instance Public Details

1. Go to **Instances**.
2. Select the running instance.
3. Copy the **Public IPv4 address** or **Public DNS**.

---

## Step 5: Locate the Key Pair File

1. Open terminal (WSL / Linux / macOS).
2. Verify the file exists:

   ```bash
   ls ~/Downloads/xfusion-kp.pem
   ```
3. If found, proceed to next step.

---

## Step 6: Set Correct Permissions on Key File

```bash
chmod 400 ~/Downloads/xfusion-kp.pem
```

This step is mandatory for SSH security.

---

## Step 7: Connect to EC2 Using SSH

```bash
ssh -i ~/Downloads/xfusion-kp.pem ubuntu@<EC2-Public-IP-or-DNS>
```

Example:

```bash
ssh -i ~/Downloads/xfusion-kp.pem ubuntu@ec2-34-201-104-123.compute-1.amazonaws.com
```

---

## Step 8: Verify Successful Login

After login, you should see:

```text
ubuntu@ip-172-31-xx-xx:~$
```

This confirms successful SSH access.

---

## Step 9: Common Errors and Fixes

### Error: Identity file not accessible

* Cause: Wrong file path
* Fix: Use absolute path to `.pem`

### Error: Permission denied (publickey)

* Cause: Wrong key or permissions
* Fix: Verify key pair name and run `chmod 400`

---

## Step 10: Logout from Instance

```bash
exit
```

---

## Final Outcome

✔ RSA key pair created
✔ Ubuntu EC2 instance launched
✔ Secure SSH connection established
✔ Basic AWS & DevOps concepts practiced

---

## Demo Summary (One Line)

> This demo explains how to securely launch an Ubuntu EC2 instance using an RSA key pair and connect via SSH following AWS best practices.

---
Below are **both deliverables**, written cleanly and simply so you can **paste directly into GitHub** and **explain confidently in interviews**.

---

# README.md

## AWS EC2 Ubuntu Access Using RSA Key Pair

---

## 📌 Project Overview

This demo project demonstrates how to securely launch an Ubuntu EC2 instance in AWS and connect to it using an RSA-based key pair. The project focuses on key pair management, SSH authentication, and basic troubleshooting—core skills expected from a DevOps engineer.

---

## 🎯 Objectives

* Create an RSA key pair in AWS
* Launch an Ubuntu EC2 instance using the key pair
* Connect to the instance via SSH
* Apply security best practices for key management

---

## 🛠 Tools & Technologies

* **Amazon EC2**
* Ubuntu Server 22.04 LTS
* SSH (OpenSSH)
* Local terminal (Linux / WSL / macOS)

---

## 📐 Architecture Flow

1. User creates an RSA key pair in AWS
2. AWS stores the public key with the EC2 instance
3. Private key (`.pem`) remains on the local machine
4. SSH uses the private key for authentication

---

## 🚀 Step-by-Step Implementation

### Step 1: Create a Key Pair

* Key pair name: `xfusion-kp`
* Key type: `RSA`
* Private key file: `xfusion-kp.pem`
* Download and store the file securely

---

### Step 2: Launch Ubuntu EC2 Instance

* Select Ubuntu Server AMI
* Choose instance type (e.g., `t2.micro`)
* Select key pair: `xfusion-kp`
* Allow SSH (port 22) in security group
* Launch the instance

---

### Step 3: Set Key File Permissions

```bash
chmod 400 ~/Downloads/xfusion-kp.pem
```

---

### Step 4: Connect to the Instance

```bash
ssh -i ~/Downloads/xfusion-kp.pem ubuntu@<EC2-Public-IP-or-DNS>
```

---

## ❗ Common Issues & Fixes

| Issue                         | Cause                    | Solution                    |
| ----------------------------- | ------------------------ | --------------------------- |
| Identity file not accessible  | Incorrect path           | Use absolute file path      |
| Permission denied (publickey) | Wrong key or permissions | Verify key pair & run chmod |
| SSH timeout                   | Port 22 blocked          | Update security group       |

---

## 🔐 Security Best Practices

* Never share `.pem` files
* Do not upload keys to GitHub
* Restrict SSH access to known IPs
* Use different key pairs per environment

---

## 📚 Learning Outcomes

* Understood EC2 key pair lifecycle
* Learned SSH authentication mechanism
* Practiced real-world troubleshooting
* Followed AWS security standards

---

## 🏁 Conclusion

This project demonstrates secure EC2 access using SSH key pairs and reflects foundational AWS and DevOps operational knowledge.

---

## 🔮 Future Improvements

* Use AWS SSM Session Manager (keyless access)
* Automate EC2 creation with Terraform
* Implement key rotation strategy

---

---

# Interview Explanation (Simple & Strong)

### Q: What is this project about?

**Answer:**
This project demonstrates how to securely access an Ubuntu EC2 instance using an RSA key pair. It focuses on AWS key management, SSH authentication, and security best practices.

---

### Q: Why do we use key pairs in AWS?

**Answer:**
AWS key pairs enable secure, password-less authentication. The public key is stored on the EC2 instance, and the private key stays with the user. This ensures strong access control.

---

### Q: What happens if the `.pem` file is lost?

**Answer:**
AWS does not allow re-downloading private keys. If the `.pem` file is lost, the instance cannot be accessed and must be relaunched with a new key pair.

---

### Q: Why is `chmod 400` required?

**Answer:**
SSH enforces strict file permissions. If a private key is readable by others, SSH rejects it to prevent security risks.

---

### Q: Why did you choose Ubuntu?

**Answer:**
Ubuntu is widely used in production environments, has long-term support, and is well-documented, making it ideal for DevOps workloads.

---

### Q: How would you improve this setup in production?

**Answer:**
I would replace SSH key access with AWS Systems Manager Session Manager, automate provisioning using Terraform, and implement key rotation policies.

---

### One-Line Summary (Very Strong)

> “I implemented secure SSH access to an Ubuntu EC2 instance using RSA key pairs and followed AWS security best practices while troubleshooting real-world access issues.”

---

If you want next, I can:

* Convert this into **portfolio bullets**
* Add **screenshots checklist**
* Create **Terraform version**
* Prepare **AWS viva questions**

Just tell me.

