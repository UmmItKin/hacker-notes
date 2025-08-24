# Null byte termination

A technique used to bypass input validation by appending a null byte (`%00`) to the end of a string. 

bypasses file extension checks in vulnerable PHP versions by truncating the file path, allowing access to unintended files (e.g., /etc/flag2 instead of a .php file). It doesn't redirect to another site but tricks the server into loading a different local file directly on the same page.
