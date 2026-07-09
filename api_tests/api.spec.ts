```typescript
import { test, expect, request } from '@playwright/test';

test.describe('Login API tests', () => {
  let apiContext: request.APIRequestContext;

  test.beforeAll(async ({ playwright }) => {
    apiContext = await playwright.request.newContext({
      baseURL: 'http://localhost', // Cambiar al host adecuado
    });
  });

  test.afterAll(async () => {
    await apiContext.dispose();
  });

  test('POST /login - positive: valid payload returns 200 and response body', async () => {
    const payload = {
      username: 'validUser',
      password: 'validPassword',
    };

    const response = await apiContext.post('/login', { data: payload });
    expect(response.status()).toBe(200);
    const body = await response.json();

    expect(body).toBeDefined();
    expect(typeof body).toBe('object');
    // Se asume que debe devolver token o info relacionada al login
    expect(body).toHaveProperty('token');
    expect(typeof body.token).toBe('string');
  });

  test('POST /login - negative: missing username returns 400', async () => {
    const payload = {
      password: 'validPassword',
    };

    const response = await apiContext.post('/login', { data: payload });
    expect(response.status()).toBe(400);
    const body = await response.json();

    expect(body).toBeDefined();
    expect(body).toHaveProperty('error');
    expect(typeof body.error).toBe('string');
  });

  test('POST /login - negative: missing password returns 400', async () => {
    const payload = {
      username: 'validUser',
    };

    const response = await apiContext.post('/login', { data: payload });
    expect(response.status()).toBe(400);
    const body = await response.json();

    expect(body).toBeDefined();
    expect(body).toHaveProperty('error');
    expect(typeof body.error).toBe('string');
  });

  test('POST /login - negative: invalid credentials returns 401', async () => {
    const payload = {
      username: 'invalidUser',
      password: 'wrongPassword',
    };

    const response = await apiContext.post('/login', { data: payload });
    expect(response.status()).toBe(401);
    const body = await response.json();

    expect(body).toBeDefined();
    expect(body).toHaveProperty('error');
    expect(typeof body.error).toBe('string');
  });

  test('POST /login - negative: empty payload returns 400', async () => {
    const response = await apiContext.post('/login', { data: {} });
    expect(response.status()).toBe(400);
    const body = await response.json();

    expect(body).toBeDefined();
    expect(body).toHaveProperty('error');
    expect(typeof body.error).toBe('string');
  });
});
```