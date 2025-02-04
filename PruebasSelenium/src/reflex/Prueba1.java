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
    public static final String INDEX = "http://localhost:3000/";
	public static final String BUSCADORES = "http://localhost:3000/buscadores/";
	public static final String REDES = "http://localhost:3000/redes_sociales/";
	static WebDriver driver;

    @BeforeAll
    static void inicializarDriver() {
        driver = new ChromeDriver();
    }

    @Test
    void verificarEnlaceBuscadores() {
        driver.get(INDEX);
        WebElement enlaceBuscadores = driver.findElement(By.id("enlaceBuscadores"));
        assertEquals(INDEX, driver.getCurrentUrl());
    }

    @Test
    void verificarEnlaceRedes() {
        driver.get(INDEX);
        WebElement enlaceRedes = driver.findElement(By.id("enlaceRedes"));
        assertEquals(INDEX, driver.getCurrentUrl());
    }

    @Test
    void verificarPaginaBuscadores() {
        driver.get(BUSCADORES);
        assertEquals(BUSCADORES, driver.getCurrentUrl());
    }

    @Test
    void verificarPaginaRedesSociales() {
        driver.get(REDES);
        assertEquals(REDES, driver.getCurrentUrl());
    }

    @Test
    void probarEnlaceBuscadores() {
        driver.get(INDEX);
        driver.findElement(By.id("enlaceBuscadores")).click();
        assertEquals(INDEX, driver.getCurrentUrl());
    }

    @Test
    void probarEnlaceRedes() {
        driver.get(INDEX);
        driver.findElement(By.id("enlaceRedes")).click();
        assertEquals(INDEX, driver.getCurrentUrl());
    }

    @Test
    void verificarEnlacesPaginaBuscadores() {
        driver.get(BUSCADORES);
        driver.findElement(By.id("google"));
        driver.findElement(By.id("bing"));
        driver.findElement(By.id("baidu"));
        driver.findElement(By.id("volver"));
        assertEquals(BUSCADORES, driver.getCurrentUrl());
    }

    @Test
    void probarEnlaceGoogle() {
        driver.get(BUSCADORES);
        driver.findElement(By.id("google")).click();
        assertEquals("https://www.google.com/", driver.getCurrentUrl());
    }

    @Test
    void probarEnlaceBing() {
        driver.get(BUSCADORES);
        driver.findElement(By.id("bing")).click();
        assertEquals("https://www.bing.com/?brdr=1", driver.getCurrentUrl());
    }

    @Test
    void probarEnlaceBaidu() {
        driver.get(BUSCADORES);
        driver.findElement(By.id("baidu")).click();
        assertEquals("https://www.baidu.com/", driver.getCurrentUrl());
    }

    @Test
    void probarEnlaceVolverBuscadores() {
        driver.get(BUSCADORES);
        driver.findElement(By.id("volver")).click();
        assertEquals(BUSCADORES, driver.getCurrentUrl());
    }

    @Test
    void verificarEnlacesPaginaRedes() {
        driver.get(REDES);
        driver.findElement(By.id("instagram"));
        driver.findElement(By.id("facebook"));
        driver.findElement(By.id("tiktok"));
        driver.findElement(By.id("volver"));
        assertEquals(REDES, driver.getCurrentUrl());
    }

    @Test
    void probarEnlaceInstagram() {
        driver.get(REDES);
        driver.findElement(By.id("instagram")).click();
        assertEquals("https://www.instagram.com/", driver.getCurrentUrl());
    }

    @Test
    void probarEnlaceFacebook() {
        driver.get(REDES);
        driver.findElement(By.id("facebook")).click();
        assertEquals("https://www.facebook.com/", driver.getCurrentUrl());
    }

    @Test
    void probarEnlaceTikTok() {
        driver.get(REDES);
        driver.findElement(By.id("tiktok")).click();
        assertEquals("https://www.tiktok.com/explore", driver.getCurrentUrl());
    }

    @Test
    void probarEnlaceVolverRedes() {
        driver.get(REDES);
        driver.findElement(By.id("volver")).click();
        assertEquals(REDES, driver.getCurrentUrl());
    }
}