```typescript
import { test, expect } from '@playwright/test';

test.describe('Login de usuario', () => {
  // Background setup data
  const validUser = 'usuarioValido';
  const validPassword = 'Password123';
  const blockedUser = 'usuarioBloqueado';

  // URL de la página de login
  const loginUrl = '/login';

  // Selectores
  const selectors = {
    usernameInput: 'input[name="username"]',
    passwordInput: 'input[name="password"]',
    loginButton: 'button[type="submit"]',
    errorMessage: '.error-message',
  };

  /**
   * Helper to perform login with given username and password
   */
  async function performLogin(page, username: string, password: string) {
    if (username !== null) {
      await page.fill(selectors.usernameInput, username);
    }
    if (password !== null) {
      await page.fill(selectors.passwordInput, password);
    }
    await page.click(selectors.loginButton);
  }

  test.beforeEach(async ({ page }) => {
    // Navigate to the login page before each test
    await page.goto(loginUrl);
  });

  test('Login exitoso', async ({ page }) => {
    // El usuario válido ingresa contraseña correcta y accede
    await performLogin(page, validUser, validPassword);
    // Asumimos que tras login exitoso redirige a dashboard o similar
    await expect(page).toHaveURL(/.*dashboard/);
  });

  test('Login con contraseña inválida', async ({ page }) => {
    // Usuario válido ingresa contraseña incorrecta
    await performLogin(page, validUser, 'ContraseñaIncorrecta');
    // Verificar mensaje de error específico
    await expect(page.locator(selectors.errorMessage)).toHaveText('Contraseña incorrecta');
  });

  test('Login con usuario bloqueado', async ({ page }) => {
    // Usuario bloqueado intenta iniciar sesión con cualquier contraseña
    await performLogin(page, blockedUser, 'CualquierContraseña');
    // Verificar mensaje de error por usuario bloqueado
    await expect(page.locator(selectors.errorMessage)).toHaveText('Usuario bloqueado');
  });

  test('Login con usuario vacío', async ({ page }) => {
    // Campo usuario vacío, contraseña válida
    await performLogin(page, '', validPassword);
    // Verificar error por usuario requerido
    await expect(page.locator(selectors.errorMessage)).toHaveText('Nombre de usuario requerido');
  });

  test('Login con contraseña vacía', async ({ page }) => {
    // Usuario válido con contraseña vacía
    await performLogin(page, validUser, '');
    // Verificar mensaje de error por contraseña requerida
    await expect(page.locator(selectors.errorMessage)).toHaveText('Contraseña requerida');
  });

  test('Login con usuario y contraseña vacíos', async ({ page }) => {
    // Ambos campos vacíos
    await performLogin(page, '', '');
    // Verificar mensaje de error que ambos campos son requeridos
    await expect(page.locator(selectors.errorMessage)).toHaveText('Nombre de usuario y contraseña requeridos');
  });
});
```