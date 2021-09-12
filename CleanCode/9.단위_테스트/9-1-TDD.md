# 단위 테스트

## TDD, Test Driven Development
* 첫째, 실패하는 단위 테스트를 작성할 때까지 서비스 코드를 작성하지 마라.
* 둘째, 컴파일은 실패하지 않으면서 실행이 실패하는 정도로만 단위 테스트를 작성 하라.
* 셋째, 현재 실패하는 테스트를 통과할 정도의 서비스 코드를 작성 하라.

이렇게 일을 하면 테스트 수천개의 케이스가 생기는데 이를 전부 다 방치를 하면 서비스 코드와 맞먹을 정도의 규모가 되는데 이는 심각한 관리문제를 야기한다.

## 깨끗한 테스트 코드
테스트 코드는 가독성이 중요하다.

변경 전은 addPage와 assertSubString를 부르는라 중복되는 코드가 매우 많다.  
자질구레한 사항은 없애고 테스트 코드 표현의 중점하자.
```java
public void testGetPageHieratchyAsXML() throws Exception
{
    crawler.addPage(root, PathParser.parse("PageOne"));
    crawler.addPage(root, PathParser.parse("PageOne.ChildOne"));
    crawler.addPage(root, PathParser.parse("PageTwo"));

    request.setResource("root");
    request.addInput("type", "pages");

    Responder responder = new SerializedPageResponder();
    SimpleResponse response = (SimpleResponse) responder.makeResponse(new FitNesseContext(root), request))
    String xml = response.getContent();

    assertEquals("text/html", response.getContentType());
    assertSubString("<name>PageOne</name>", xml);
    assertSubString("<name>PageTwo</name>", xml);
    assertSubString("<name>ChildOne</name>", xml);
}
```

변경 후
```java
public void testGetPageHieratchyAsXML() throws Exception
{
    makePages("PageOne", "PageOne.ChildOne", "PageTwo");
    submitRequest("root", "type:pages")

    assertResponseIsXML();
    assertResponseContains(
        "<name>PageOne</name>","<name>PageTwo</name>","<name>ChildOne</name>"
    );
}
```