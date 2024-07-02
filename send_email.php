<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form data
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    // Your email address
    $to = "jose.reyesfabian@gmail.com";
    $subject = "New Contact Form Submission";

    // Construct the email content
    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n\n";
    $email_content .= "Message:\n$message\n";

    // Construct the email headers
    $email_headers = "From: $name <$email>";

    // Send the email
    if (mail($to, $subject, $email_content, $email_headers)) {
        // Redirect to a thank-you page (optional)
        header("Location: thank_you.html");
        exit;
    } else {
        echo "Oops! Something went wrong and we couldn't send your message.";
    }
}
?>
