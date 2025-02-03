package reflex;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Prueba1 {
	static WebDriver driver1;

	@BeforeAll
	static void setURL() {
		driver1 = new ChromeDriver();
		driver1.get("http://localhost:3000/");
	}

	@Test
	void test1() {
		
		WebElement indexCorrecto = driver1.findElement(By.id("enlaces"));
        String textoIndex = indexCorrecto.getText();
        assertEquals("Enlaces favoritos", textoIndex);
	}

}
