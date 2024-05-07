SELECT 
    grantee,
    privilege_type
FROM 
    information_schema.user_privileges
WHERE 
    grantee LIKE 'user\_0d\_1@localhost' OR grantee LIKE 'user\_0d\_2@localhost';

