# IDORs

Like XSS, IDOR is a vulnerability that is often found in web applications and very common and begin ignored by developers. IDOR stands for `Insecure Direct Object Reference`. This vulnerability occurs when an application provides direct access to objects based on user-supplied input. As a result of this vulnerability, attackers can bypass authorization and access resources in the system directly, for example, user data could not verify the user's authorization. So the attacker can access other users' data.

Normally, when a user requests a resource, the application should verify that the user has the necessary permissions to access the resource. However, in the case of IDOR, the application does not verify the user's permissions, allowing the attacker to access the resource directly.

## Change the Requested Object

The most common way to exploit IDOR is to change the requested object. For example, suppose an application has an endpoint that allows users to access their receipts:

```
GET /get_receipt?receipt_id=2952
https://example.com/get_receipt?receipt_id=2952
```

In this case, the application should verify that the user has the necessary permissions to access the receipt with ID 2952. However, if the application does not verify the user's permissions, an attacker can simply change the receipt_id parameter to access other users' receipts:

```
GET /get_receipt?receipt_id=2953
https://example.com/get_receipt?receipt_id=2953
```

In this case, the attacker can access the receipt with ID 2953 without the necessary permissions.

## Wordpress IDOR

Wordpress is a popular content management system that is used by millions of websites. Wordpress has a vulnerability that allows attackers to access other users' data. This vulnerability is known as Wordpress IDOR.

As the example we can use the following URL:

```
GET /wp-json/wp/v2/users/10
https://hereis.wordpress.com/wp-json/wp/v2/users/10
```

That is the API endpoint that allows users to access user data. You got the details of this user with ID 10 without the necessary permissions, not even being logged in or authenticated.

This vulnerability is very dangerous because it allows attackers to access sensitive information such as user emails, passwords, and other personal data. and can be Targeted the username enumeration. not even need to be authenticated.

Those information should be protected and only accessible to the user who owns the data. But in wordpress, they are accessible to anyone who knows the user ID. which is a big security issue.

```json
{
  "id": 10,
  "name": "New name",
  "url": "",
  "description": "This is the new user description.",
  "link": "https://hereis.wordpress/link",
  "slug": "new-slug-123456",
  "avatar_urls": {
    "24": "//hereis.wordpress.com/wp-content/uploads/member/avatars/new-avatar-24.jpg",
    "48": "//hereis.wordpress.com/wp-content/uploads/member/avatars/new-avatar-48.jpg",
    "96": "//hereis.wordpress.com/wp-content/uploads/member/avatars/new-avatar-96.jpg"
  },
  "meta": [],
  "_links": {
    "self": [
      {
        "href": "https://hereis.wordpress.com/wp-json/wp/v2/users/10",
        "targetHints": {
          "allow": [
            "GET"
          ]
        }
      }
    ],
    "collection": [
      {
        "href": "https://hereis.wordpress.com/wp-json/wp/v2/users"
      }
    ]
  }
}
```

Attacker can launch a brute force attack to get the user ID and then access the user data. This API is worse than the previous example because it allows attackers to access all users' data, not just one user's data.

Also, is that meaning you can write your own script to fetching all users' data by changing the user ID in the URL? A very serious vulnerability that should blocked by the default.
