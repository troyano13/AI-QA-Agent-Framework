# Coverage Analysis

**Historia de usuario:**
- Cubiertos los criterios principales: login exitoso, password inválido, usuario bloqueado.

**Casos de prueba (Gherkin):**
- Escenarios positivos y negativos están bien definidos.
- Incluye validación de campos vacíos para usuario, contraseña y ambos.
- Escenarios aprobados abarcan:
  - Login exitoso.
  - Password inválido.
  - Usuario bloqueado.
  - Usuario vacío.
  - Contraseña vacía.
  - Usuario y contraseña vacíos.

**Automatización UI:**
- Copia fiel de los escenarios de Gherkin.
- Maneja el flujo completo desde llenar campos hasta verificar mensajes o URL.
- Verifica redirección en login exitoso.
- Validación de mensajes de error es consistente para todos los casos.

**Automatización API:**
- Buen rango de casos:
  - Login exitoso (código 200).
  - Username faltante (400).
  - Password faltante (400).
  - Credenciales inválidas (401).
  - Payload vacío (400).
- Validación de cuerpo de respuesta, propiedades y tipos.
- No cubre directamente usuario bloqueado (un caso relevante en UI y historia).

---

# Missing Scenarios

1. **API: Usuario bloqueado**
   - No hay prueba API para usuario bloqueado (esperar 403 o similar con mensaje adecuado).
2. **API: Usuario con campo username vacío (string vacío)**
   - Se prueba ausencia del campo, no valor vacío. Similar para password.
3. **UI y API: Validación de formato de usuario (e.g., usuario con espacio, caracteres no válidos)**
   - No está contemplado.
4. **UI y API: Caso de tiempo de espera / error servidor**
   - No se prueba.
5. **UI: Verificar que el campo password tiene tipo password (no visible en el código pero recomendable)**
6. **UI: Prueba de usabilidad – foco, labels, accesibilidad**
   - No existen pruebas funcionales aparte del login.

---

# Risks

- **Inconsistencia entre UI y API en caso de usuario bloqueado:** API no valida ni reporta usuario bloqueado. Riesgo funcional si backend no previene acceso.
- **Estados del sistema no definidos:** No se maneja qué pasa si backend está caído o responde tardíamente.
- **Falta prueba de casos límite o formatos inválidos:** Podrían generar bugs de validación.
- **Posible duplicidad o confusión en mensajes de error si la UI y el API no manejan igual la lógica.**
- **No se cubre concurrency/rate limiting ni bloqueo progresivo tras múltiples intentos fallidos.**

---

# Automation Improvements

- **Parámetros en helper 'performLogin':**
  - En UI, para username y password se pasa null para evitar llenar, pero en escenario vacío se usa string vacía. Consistencia recomendable (si se quiere borrar o no campo).
- **Agregar validaciones UI para accesibilidad y validación de atributos (ej. verificar tipo="password") mediante playwright.**
- **Extraer URLs y mensajes de error a variables o archivos de configuración para facilitar mantenimiento.**
- **Agregar test de role-based access si aplica (usuario diferente tipos).**
- **API tests: Agregar pruebas para usuario bloqueado con respuesta adecuada.**
- **API: Verificar headers u otros aspectos de seguridad (tokens, CORS, etc.).**
- **Testear respuestas de error con contenido internacionalizado si se aplica.**

---

# Final Score (0-100)

- Historia y casos: 95 (bien planteado).
- Gherkin: 90 (excelente, pero le falta cubrir casos límite y validaciones extra).
- UI Automation: 90 (completo pero con pequeñas mejoras).
- API Automation: 80 (buen conjunto pero falta usuario bloqueado y validaciones de formato).
- Riesgos y missing escenarios restan puntos.

**Puntaje final:** 87/100

---

# Recommendations

1. **Agregar test API para usuario bloqueado.** Es crítico para asegurar que backend bloquea acceso y responde con código y mensaje adecuado.
2. **Incluir validaciones para campos con valores vacíos explícitos ("") y formato inválido.**
3. **Agregar pruebas negativas adicionales (usuarios con formatos inválidos, SQL injection, datos no ascii).**
4. **Verificar aspectos de UI relacionados a accesibilidad y controles (tipo password, labels, foco, mensajes amistosos).**
5. **Centralizar mensajes de error en archivos o constantes para facilitar mantenimiento.**
6. **Probar casos de error de red o backend lento en UI para mejorar robustez.**
7. **Revisar y validar la sincronía entre mensajes y códigos HTTP devueltos por UI y API.**
8. **Considerar pruebas para multiusuario, sesiones, y manejo de tokens tras login.**

---

¿Quieres que prepare un plan de acción detallado para mejorar la cobertura y automatización?