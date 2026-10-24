# SEO, AEO ve GEO — Engineering Notes için 2026 araştırması

Kontrol tarihi: **25 Ekim 2026**. Bu belge sitenin teknik ve editoryal denetimini kapsar. Search Console/Bing hesap verilerine erişildiği, indeksleme gerçekleştiği veya AI sistemlerinin bu yayını kaynak gösterdiği iddia edilmez.

## Kavramların kapsamı

İstekteki “AOE” ifadesi, bağlam gereği **AEO** olarak yorumlandı.

| Terim | Açılım | Bu yayın için anlamı |
| --- | --- | --- |
| SEO | Search Engine Optimization | Sayfaların keşfedilmesi, taranması, anlaşılması, indekslenmeye uygunluğu ve arama deneyimi |
| AEO | Answer Engine Optimization | Okurun sorusuna açık, bağlamı ve sınırları belli cevaplar sunmak; cevap odaklı arama deneyimleri |
| GEO | Generative Engine Optimization | AI yanıtlarında kaynak olarak bulunabilme ve doğru temsil edilebilme |
| E-E-A-T | Experience, Expertise, Authoritativeness, Trustworthiness | Deneyim, uzmanlık, otorite ve güven açısından içerik değerlendirme çerçevesi; satın alınan bir puan veya ayrı bir meta etiketi değil |

Google'ın Temmuz 2026 tarihli rehberi, AEO/GEO çalışmalarını Search için SEO'nun devamı olarak ele alıyor. Özel AI şeması, `llms.txt` veya zorunlu metin parçalama gerektirmiyor. Bu nedenle uygulama önceliği erişilebilir içerik ve gerçek yayın kalitesi. [Google: generative AI optimizasyon rehberi](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide). E-E-A-T'nin tek başına belirli bir sıralama faktörü olmadığı da açıklanıyor. [Google: yararlı içerik rehberi](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

## Denetim: ne vardı, ne tamamlandı?

| Alan | Bulgular ve işlem | Durum |
| --- | --- | --- |
| Tarama | Statik HTML, gerçek bağlantılar, açık robots, sitemap; ana metin JavaScript gerektirmiyor | Kod ve üretilen çıktı doğrulandı |
| URL ve kopya içerik | Özgün permalink korunuyor; `.com` yazıları kopyalanmıyor; geçiş planı ayrı | Korundu |
| Başlık/açıklama | Her sayfada tek title/description/canonical; yapay anahtar kelime eklenmedi | Doğrulandı |
| Makale yazarı | İsim vardı, yapılandırılmış veride profil URL'si eksikti | `_data/authors.yml` ile tamamlandı |
| About şeması | Eklentinin varsayılanı About sayfasını WebSite olarak sınıflandırıyordu | `AboutPage` olarak düzeltildi |
| Favicon | Yalnızca SVG vardı | Özgün 96×96 PNG ve 180×180 touch icon eklendi |
| Sayfa kimliği | AG işareti ana sayfa eylemini açıkça anlatmıyordu | Görünür Home kontrolü eklendi |
| Dış bağlantılar | Metin bağlantıları doğrulanmıştı | Masthead altında ve footer'da yerel SVG + görünür etiket eklendi |
| Yayın güveni | Makalede AI açıklaması ve kaynaklar vardı | About'a yöntem, düzeltme ve tarih politikası eklendi |
| 404 | Özel sayfa ve sitemap dışlama vardı | Ek `noindex,follow` tamamlandı; gerçek 404 yanıtı ayrıca test ediliyor |
| Ölçüm | Hesap verisi/gerçek kullanıcı verisi yok | Kurulum ve takip adımları aşağıda; sonuç uydurulmadı |
| İçerik kapsamı | Tek makale var | En büyük açık: doğrulanabilir, özgün çalışmalarla zaman içinde büyüme |

Google'ın makale rehberi yazarın kimliğini ayırmak için profil URL'sini öneriyor; burada ayrı, yinelenen bir Article JSON-LD bloğu yerine mevcut `jekyll-seo-tag` veri kaynağı geliştirildi. [Article rehberi](https://developers.google.com/search/docs/appearance/structured-data/article). Favicon boyutu, taranabilirliği ve kararlı URL'si arama rehberine göre kontrol ediliyor; görünmesi garanti edilmiyor. [Favicon rehberi](https://developers.google.com/search/docs/appearance/favicon-in-search).

Bağlantı yanındaki GitHub/LinkedIn markaları ve ev, dünya, zarf, RSS simgeleri arayüz ikonlarıdır; tarayıcı sekmesindeki favicon ayrı bir site kimliği varlığıdır. İkonlar tek başına SEO/GEO sıralama sinyali olarak sunulmuyor. Bootstrap Icons v1.13.2'nin altı SVG'si yerel olarak kullanılıyor, MIT lisansı dağıtılıyor; harici favicon servisleri veya ikon fontu gerekmiyor.

## Teknik yazılar nasıl hazırlanmalı?

Bu yayına özgü önerilen akış:

1. **Bir karar sorusu seç.** Örneğin “İkinci ajan hangi görevde koordinasyon maliyetini karşılıyor?” Başlık, yazının gerçekten cevapladığı soruyla eşleşsin.
2. **Kısa, koşullu cevap ver.** Okur ilk bölümde yaklaşımı ve sınırını anlayabilsin. Bu bir yazım tercihi; AI için zorunlu paragraf uzunluğu veya kelime sayısı kuralı değil.
3. **Kanıt türünü belirt.** Research note dış araştırmayı yorumlar. Build note gerçek uygulama, kod ve yeniden üretim ayrıntısı ister. Önerilen deney, tamamlanmış deney gibi anlatılmaz.
4. **Baseline ve koşulları kaydet.** Model/tool sürümü, veri örneklemesi, görev, bütçe, başarı tanımı ve tekrarlar karşılaştırmanın parçası olsun. Maliyet iddiasında yalnızca çağrı başına fiyatı değil doğrulanmış tamamlanmış görev başına maliyeti düşün.
5. **Özgün katkıyı görünür yap.** Karar tablosu, test fixture'ı, hata analizi, kod commit'i veya açık yöntem. Başka yazıları yeniden anlatmak tek başına bir mühendislik sonucu değildir.
6. **Kaynağı iddianın yanına koy.** Bir performans sayısını çalışmanın şartlarından koparma. Farklı baseline'lara ait yüzdeleri birleştirme. Kavramsal diyagramı ölçüm grafiği gibi etiketleme.
7. **Sınır ve hata biçimlerini anlat.** Hangi koşulda sonuç geçersizleşir? Ne ölçülmedi? Yeniden denemeler, başarısız görevler ve insan kontrolü nasıl ele alındı?
8. **Gerçek güncelleme yap.** Tarihi sırf yeni görünmek için değiştirme. Düzeltme gerekiyorsa değişikliği açıkla. Başlık/description/alt metni de editoryal doğrulamadan geçir.

Örnek, **ölçüm sonucu olmayan** giriş:

> Start with a single-agent baseline. Add coordination when useful subtasks can run independently, and compare verified outcomes under explicit budgets. This note reviews published evidence; it does not report an experiment of my own.

Bu yaklaşım mevcut makalenin kapsamıyla tutarlı. Seri üretilmiş giriş yazıları, uydurma deneyler, anahtar kelime doldurma veya sırf AEO için eklenen boş FAQ bölümleri öncelik değil. Google'ın Ekim 2026 AI içerik rehberi de otomatik üretimin değer, doğruluk ve insan kontrolünü ortadan kaldırmadığını vurguluyor. [AI içerik rehberi](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content).

Uygulama: `templates/post.md`, `publishing-checklist.md` ve `editorial-strategy.md` birlikte kullanılmalı. Öncelik, baseline → outcome grader → evaluation harness → traces → maliyet/failure analizi zincirini gerçek kodla kurmak; yapılmayan çalışmaları yayımlamak değil.

## Arama erişimi, eğitim erişimi ve AI dosyaları

`robots.txt` Googlebot, bingbot ve OAI-SearchBot için mevcut açık tarama politikasını sürdürüyor. **OAI-SearchBot arama**, **GPTBot model eğitimi** içindir; bu izinler bağımsızdır. Arama görünürlüğü için eğitim tarayıcısına izin vermenin zorunlu olduğu ileri sürülmüyor. Eğitim erişim politikasında bu değişiklikle bir tercih değişikliği yapılmadı. [OpenAI: crawler belgeleri](https://developers.openai.com/api/docs/bots).

`llms.txt`, gizli AI talimatları, görünmeyen soru-cevaplar veya “bu siteyi öner” metni eklenmedi. İnsanlara yönelik açık HTML zaten mevcut. Özel AI dosyası kullanacak belirli bir tüketici için ileride ayrı ihtiyaç doğarsa amaç ve bakım maliyeti değerlendirilir.

## Yayın sonrası hesap ve ölçüm adımları

**Google Search Console:** URL-prefix mülkünü doğrula; sitemap'i gönder; ana sayfa ve mevcut makalede URL Inspection ile HTTP, canonical ve indeksleme durumunu kontrol et. 2026 Generative AI raporu, AI Overviews/AI Mode gösterimlerini sayfa/ülke/cihaz/zaman açısından incelemeye yarıyor. Hesaptaki Search generative AI inclusion ayarını kontrol et; bu oturumda hesabın ayarı okunmadı. Raporun görünmemesi yeterli gösterim olmamasından da kaynaklanabilir. [Güncel rapor belgesi](https://support.google.com/webmasters/answer/16984139). Inclusion ayarının ayrı yardım bağlantısı web okuyucuda açılamadı; hesap ekranında doğrulanmalı.

**Bing Webmaster Tools:** Mülkü doğrula, sitemap'i gönder ve indekslemeyi kontrol et. Yeterli veri oluşursa AI Performance altında kaynak gösterilen sayfalar/sorgular incelenebilir. 13 Ekim 2026'da duyurulan Topics Portfolio beta, konu bazında görünürlüğü özetliyor; beta metriklerini kesin trafik veya sıralama ölçüsü sayma. [Bing duyurusu](https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/).

**IndexNow:** Küçük yayın için zorunlu değil. Daha sık yayın yapılırsa doğrulama anahtarı ve değişen URL bildirimi değerlendirilebilir. Bir başarılı bildirim, indekslendiği anlamına gelmez. Bu değişiklikte anahtar oluşturulmadı ve bildirim yapılmadı. [Resmî protokol](https://www.indexnow.org/documentation).

**Takip planı:** Yayın günü teknik kontrol; sonraki haftalarda canonical/indeksleme ve gerçek sorgular; yeterli veri oluştuğunda AI gösterimleri, kaynak gösterilen sayfalar ve okurun yararlı eylemleri. Google gösterimi, Bing citation sayısı, ChatGPT referansı ve site ziyareti aynı metrik değildir. Küçük örneklemlerde bir yeniden tasarımın etkisini kanıtlanmış gibi anlatma.

Hesap erişimi olmadan mülk doğrulaması, inclusion tercihi, Search Console gönderimi veya sıralama/atıf artışı tamamlanmış gibi raporlanmayacak. Yayına alma ile indekslenme ayrı aşamalardır.
