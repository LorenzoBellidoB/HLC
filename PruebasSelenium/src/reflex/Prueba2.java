package reflex;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.List;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Prueba2 {
	static WebDriver driver;
	
	public static final String INDEX = "http://localhost:3000/";
	public static final String FORM = "http://localhost:3000/formulario/";

    @BeforeAll
    static void inicializarDriver() {
        driver = new ChromeDriver();
    }

    @Test
    void verificarPageFormulario() {
    	driver.get(FORM);
    	assertEquals(FORM, driver.getCurrentUrl());
    }
    
    @Test
    void verificarTitulo() {
    	driver.get(FORM);
    	assertEquals("Formulario de registro - Mi web.", driver.getTitle());
    }
    
    @Test
    void verificarLabelNombre() {
    	driver.get(FORM);
    	WebElement lNombre = driver.findElement(By.id("lNombre"));
    	String label = lNombre.getText();
    	assertEquals("Nombre", label);
    }
    
    @Test 
    void verificarEntryNombre() {
    	driver.get(FORM);
    	WebElement iNombre = driver.findElement(By.id("iNombre"));
    	assertEquals("text", iNombre.getAttribute("type"));
    	assertEquals("50", iNombre.getAttribute("maxlength"));
    }
    
    @Test 
    void verificarLabelApellidos() {
    	driver.get(FORM);
    	WebElement lApellidos = driver.findElement(By.id("lApellidos"));
    	String label = lApellidos.getText();
    	assertEquals("Apellidos", label);
    }
    
    @Test 
    void verificarEntryApellidos() {
    	driver.get(FORM);
    	WebElement iApellidos = driver.findElement(By.id("iApellidos"));
    	assertEquals("text", iApellidos.getAttribute("type"));
    	assertEquals("50", iApellidos.getAttribute("maxlength"));
    }
    
    @Test
    void verificarLabelSexo() {
    	driver.get(FORM);
    	WebElement lSexo = driver.findElement(By.id("lSexo"));
    	String radio = lSexo.getText();
    	assertEquals("Sexo",radio);
    }
    
    @Test
    void obtenerOpcionesRadioSexo() {
        // Configurar el WebDriver (asegúrate de que el chromedriver está configurado correctamente)
     	driver.get(FORM);

     // Localizar todas las opciones de radio en Reflex
        List<WebElement> radioButtons = driver.findElements(By.id("rSexo"));

        // Extraer y mostrar las opciones disponibles
        for (WebElement radio : radioButtons) {
            System.out.println(radio.getText());
        }

    }
    
    @Test 
    void verificarEntryCorreo() {
    	driver.get(FORM);
    	WebElement iCorreo = driver.findElement(By.id("iCorreo"));
    	assertEquals("text", iCorreo.getAttribute("type"));
    }
    
    @Test
    void verificarLabelCorreo() {
    	driver.get(FORM);
    	WebElement lCorreo = driver.findElement(By.id("lCorreo"));
    	String correo = lCorreo.getText();
    	assertEquals("Correo",correo);
    }
    
    @Test 
    void verificarCheck() {
    	driver.get(FORM);
    	WebElement iCasilla = driver.findElement(By.id("iCasilla"));
    	assertEquals("button", iCasilla.getAttribute("type"));
    	assertEquals("true", iCasilla.getAttribute("aria-checked"));
    }
    
    @Test
    void verificarLabelCheck() {
    	driver.get(FORM);
    	WebElement lCasilla = driver.findElement(By.id("lCasilla"));
    	String casilla = lCasilla.getText();
    	assertEquals("Deseo recibir información sobre novedades y ofertas",casilla);
    }
    
    @Test 
    void verificarCheck2() {
    	driver.get(FORM);
    	WebElement iCasilla = driver.findElement(By.id("iCasilla2"));
    	assertEquals("button", iCasilla.getAttribute("type"));
    }
    
    @Test
    void verificarLabelCheck2() {
    	driver.get(FORM);
    	WebElement lCasilla = driver.findElement(By.id("lCasilla2"));
    	String casilla = lCasilla.getText();
    	assertEquals("Declaro haber leido y aceptar las condiciones generales del programa y la normativa sobre protección de datos",casilla);
    }
    
    @Test 
    void verificarButton() {
    	driver.get(FORM);
    	WebElement iButton = driver.findElement(By.id("iButton"));
    	assertEquals("submit", iButton.getAttribute("type"));
    }
    
}