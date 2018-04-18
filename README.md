# BEM - DIY
Web Portal for Badan Eksekutif Mahasiswa D.I Yogyakarta

### Create Database
```sql
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```

### TODO
- [ ] Post by category
- [ ] Post by tag
- [ ] Change author to devisi
- [ ] Send email in contact page
- [ ] Pagination
- [ ] Search
- [ ] Make dynamic content for header-footer
- [ ] Subscription on footer