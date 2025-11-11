# TODO: validate
# Acme – Online Food Delivery Platform
## Testing Strategy

### 1. Objective
The goal of this testing strategy is to ensure that all features of the application work well.<br>
Tested features include:
- product catalog
- cart
- checkout
- delivery

---

### 2. Scope

**In Scope:**
- Functional and non-functional testing of all Django backend modules.  
- UI and UX validation for HTML/CSS frontend.  
- Integration between components: accounts, products, payments (future integration).  
- Data integrity and business logic verification in SQLite database.  
- Unit, Integration, performance, and security testing for production readiness.

**Out of Scope:**
- Third-party payment system testing (future implementation) 
- Load testing beyond small-to-medium user base (due to SQLite limitations).  

---

### 3. Testing Levels

| Level                   | Description                                                                                | Example                                                                   |
|-------------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **Unit Testing**        | Test individual Django models, views, and utility functions (80%+ coverage)                | Verify `Order.calculate_total()` returns correct total.                   |
| **Integration Testing** | Validate interaction between modules (e.g., accounts–products–payments integration).       | Confirm only an authenticated user can place an order.                    |
| **Performance Testing** | End-to-end testing of complete workflows with multiple users (small-to-medium user count). | Verify that an application works well under moderate load                 |
| **Security Testing**    | Ensure the application is protected against vulnerabilities like unauthorized access, CSRF, SQL injection, and weak authentication flows. | Attempt to access admin pages without login or submit form without CSRF token and verify access is denied. |

---

### 4. Testing Types

1. **Unit Testing**
   - Test Django models, views, and utility functions individually.  
   - Validate core logic such as order total calculation and product stock updates.  
   - Target test coverage: at least 80%.  

2. **Integration Testing**
   - Verify interactions between modules (e.g., accounts, products and the integration of these modules).  
   - Confirm only authenticated users can perform restricted actions (e.g., place an order).  
   - Ensure data flows correctly between components and database.  

3. **Performance Testing**
   - Evaluate how the application performs under a moderate number of concurrent users.  
   - Measure response times for key workflows such as browsing products and checkout.  
   - Identify performance bottlenecks in the Django backend or database queries.  

4. **Security Testing**
   - Check protection against unauthorized access, CSRF attacks, and SQL injection.  
   - Validate proper session handling, password hashing, and permission management.  
   - Attempt to access restricted areas (e.g., admin pages) or submit forms without CSRF tokens or required roles to ensure access is denied.

---

### 5. Test Environment

| Component | Details                                            |
|------------|----------------------------------------------------|
| **Backend** | Python 3.x, Django (latest LTS version)            |
| **Database** | SQLite (development/testing)                       |
| **Frontend** | HTML, CSS                                          |
| **OS** | Windows / Linux                                    |
| **Browser** | Chrome, Firefox, Safari                            |
| **Tools** | Pytest, Django TestCase, Selenium, Postman, Locust |

---

### 6. Test Data Management
- Seed initial data with Django fixtures (e.g., N users, M products).  
- Anonymize user data during testing.  
- Reset the database after each test run to maintain consistency.  

---

### 7. Test Case Examples

| ID | Module | Test Description | Expected Result                         | Type |
|----|---------|------------------|-----------------------------------------|------|
| TC001 | Authentication | Register new user | User created, redirected to dashboard   | Functional |
| TC003 | Cart | Add product to cart | Product appears with correct quantity   | Functional |
| TC004 | Order | Place order | Order created and status = “Order sent” | Integration |
| TC005 | Payment | Checkout with online payment | Payment success, order status = “Paid”  | System |
| TC006 | UI | Validate layout consistency | All elements aligned and readable       | UI |
| TC007 | Security | Access admin page as user | Access denied                           | Security |

---

### 8. Automation Strategy

- **Framework:** `pytest-django` for backend unit/integration tests.  
- **UI Testing:** Selenium for browser-based functional tests.  
- **Continuous Integration:** GitHub Actions.  
- **Trigger:** Automated tests run on every pull request and deployment.  

---

### 9. Defect Management

| Step | Tool               | Action                                                       |
|------|--------------------|--------------------------------------------------------------|
| Defect Logging | Jira               | Record defect with steps and environment create a bug report |
| Review & Triage | QA + Dev           | Assign priority (Critical, Major, Minor)                     |
| Fix Verification | QA                 | Retest and close after confirmation                          |

---

### 10. Exit Criteria
Testing is considered complete when:
- All critical and major defects are fixed.  
- Functional coverage ≥ 80%.  
- Regression suite passes 100%.
- Test Report are sent to stakeholders and is approved by them
---

### 11. Reporting
- **Daily Test Progress Report** – executed tests, open defects, blockers.  
- **Final Test Summary Report** – test coverage, defect statistics, pass/fail rate.  

---

### 12. Risks and Mitigation

| Risk | Impact | Mitigation |
|------|---------|-------------|
| Limited test data variety | Medium | Use dynamic data generation scripts |
| SQLite concurrency limitations | Low | Use PostgreSQL in staging |
| Manual UI testing delays | Medium | Automate key flows with Selenium |

---

### 13. Roles & Responsibilities

| Role | Responsibility                                                               |
|------|------------------------------------------------------------------------------|
| **QA Engineer** | Write and execute test cases, manage test data                               |
| **Developer** | Write unit tests, fix defects, resolve bugreports                            |
| **Project Manager** | Monitor quality metrics, approve test reports, communicate with stakeholders |

---

### 14. Deliverables
- Test Plan Document  
- Test Case Suite  
- Test Data Set (fixtures)  
- Test Execution Reports  
- Defect Logs  
- Final Test Summary  

---
