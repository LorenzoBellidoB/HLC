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

        // Cerrar el navegador
        driver.quit();
    }
    
}