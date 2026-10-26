# OpenClaw 🦞 — Trợ lý AI của bạn, trên thiết bị và ứng dụng trò chuyện của bạn

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-banner-light.png">
    <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-banner-dark.png" alt="OpenClaw — Trợ lý AI chạy trên thiết bị của chính bạn.">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/openclaw/openclaw/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/openclaw/openclaw/ci.yml?branch=main&style=flat-square&label=ci" alt="Trạng thái CI"></a>
  <a href="https://www.npmjs.com/package/openclaw"><img src="https://img.shields.io/npm/v/openclaw?style=flat-square&label=npm" alt="Phiên bản npm"></a>
  <a href="https://nodejs.org"><img src="https://img.shields.io/node/v/openclaw?style=flat-square" alt="Phiên bản Node.js"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="Giấy phép MIT"></a>
  <a href="https://discord.gg/clawd"><img src="https://img.shields.io/discord/1456350064065904867?label=discord&logo=discord&logoColor=white&color=5865F2&style=flat-square" alt="Discord"></a>
</p>

OpenClaw là trợ lý AI mã nguồn mở chạy trên máy tính của bạn và kết nối với những nền tảng trò chuyện bạn đang dùng, như Discord, iMessage, Slack, Teams, Telegram, WhatsApp và hơn 20 nền tảng khác. OpenClaw cũng có ứng dụng dành cho macOS, iOS, Android, Windows và Linux. Một Gateway có thể vận hành như trợ lý cá nhân trên laptop hoặc triển khai dùng chung cho cả nhóm; điểm khác biệt chủ yếu nằm ở cấu hình.

**Bạn toàn quyền kiểm soát.** Trạng thái, bộ nhớ và thông tin xác thực được lưu trên phần cứng của bạn. Bạn có thể thay đổi mô hình AI và bộ công cụ tác tử (như Claude, Codex hoặc mô hình chạy cục bộ) dưới dạng plugin mà không cần thay đổi phần còn lại. Nội dung yêu cầu được gửi đến nhà cung cấp mô hình và nền tảng trò chuyện mà bạn cấu hình, cùng dữ liệu chẩn đoán nếu bạn tự bật xuất dữ liệu. Theo mặc định, OpenClaw chỉ tự kiểm tra phiên bản hằng ngày; thống kê tính năng ẩn danh là tùy chọn. Đặt `update.checkOnStart: false` sẽ tắt cả hai chức năng này. Xem [dữ liệu OpenClaw gửi đi](https://docs.openclaw.ai/gateway/telemetry).

OpenClaw được quản lý bởi [OpenClaw Foundation](https://openclaw.org), một tổ chức độc lập theo diện 501(c)(3). Dự án không có gói trả phí, dịch vụ lưu trữ do dự án vận hành hay token riêng. Tìm hiểu lý do thiết kế tại [Vì sao chọn OpenClaw](https://docs.openclaw.ai/start/why-openclaw).

[Trang web](https://openclaw.ai) · [Tài liệu](https://docs.openclaw.ai) · [Bắt đầu](https://docs.openclaw.ai/start/getting-started) · [Vì sao chọn OpenClaw](https://docs.openclaw.ai/start/why-openclaw) · [Câu hỏi thường gặp](https://docs.openclaw.ai/help/faq) · [Tầm nhìn dự án](VISION.md) · [DeepWiki](https://deepwiki.com/openclaw/openclaw)

## Cài đặt

Trình cài đặt hỗ trợ macOS, Linux và Windows. Khi cần, trình cài đặt sẽ thiết lập môi trường Node.js tương thích.

```bash
# macOS / Linux / WSL2
curl -fsSL https://openclaw.ai/install.sh | bash
```

```powershell
# Windows PowerShell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

Nếu bạn đã quản lý Node.js, có thể cài trực tiếp gói đã phát hành (cần Node 24.16+ hoặc 26.1+; khuyến nghị Node 26):

```bash
npm install -g openclaw@latest --allow-scripts=openclaw
```

Lệnh trên dành cho npm 12 hoặc npm 11.16 trở lên. Với npm 11.15 trở xuống, hãy bỏ `--allow-scripts=openclaw`. Xem [hướng dẫn cài đặt](https://docs.openclaw.ai/install) để biết về quy trình script vòng đời, Docker, Nix và các cách triển khai khác.

## Bắt đầu nhanh

Sau khi cài mới, các tập lệnh cài đặt sẽ tự khởi chạy quá trình thiết lập. Hãy hoàn tất trình hướng dẫn được mở ra. Nếu cài gói trực tiếp bằng npm, pnpm hoặc Bun, hãy chạy:

```bash
openclaw onboard --install-daemon
```

Sau khi thiết lập xong:

```bash
openclaw gateway status
openclaw dashboard
```

Trình thiết lập sẽ kiểm tra quyền truy cập mô hình, tạo không gian làm việc và cấu hình Gateway. Lệnh cuối cùng mở giao diện điều khiển; hãy gửi thử một tin nhắn để xác nhận trợ lý hoạt động bình thường. Xem [hướng dẫn bắt đầu](https://docs.openclaw.ai/start/getting-started) để thiết lập kênh trò chuyện và xử lý sự cố.

## OpenClaw hoạt động như thế nào?

- [Gateway](https://docs.openclaw.ai/gateway) là trung tâm điều khiển cục bộ, quản lý phiên làm việc, công cụ, sự kiện và kết nối các kênh.
- [Giao diện điều khiển](https://docs.openclaw.ai/web/control-ui), CLI và [TUI](https://docs.openclaw.ai/web/tui) kết nối với Gateway.
- [Các kênh](https://docs.openclaw.ai/channels) đưa trợ lý đến WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage và các dịch vụ nhắn tin khác.
- [Ứng dụng đồng hành và nút thiết bị](https://docs.openclaw.ai/platforms) bổ sung tính năng giọng nói, Canvas, camera, màn hình và thao tác trực tiếp trên thiết bị ở những nền tảng được hỗ trợ.

OpenClaw tương thích với [nhà cung cấp mô hình AI](https://docs.openclaw.ai/concepts/model-providers) chạy trên đám mây hoặc cục bộ. [Công cụ](https://docs.openclaw.ai/tools), [kỹ năng](https://docs.openclaw.ai/tools/skills) và [plugin](https://docs.openclaw.ai/plugins) giúp mở rộng khả năng của trợ lý.

## Bảo mật

Hãy xem mọi tin nhắn đến là dữ liệu đầu vào không đáng tin cậy. Theo mặc định, các kênh hỗ trợ nhắn tin trực tiếp yêu cầu ghép đôi với người gửi chưa xác định. Phê duyệt yêu cầu ghép đôi bằng lệnh:

```bash
openclaw pairing approve <channel> <code>
```

Trừ khi bạn cấu hình chế độ sandbox, các công cụ của phiên chính sẽ chạy trên máy chủ của bạn. Trước khi kết nối người dùng khác hoặc cho phép truy cập Gateway từ xa, hãy đọc [hướng dẫn bảo mật](https://docs.openclaw.ai/gateway/security), [quy trình xử lý rủi ro khi mở quyền truy cập](https://docs.openclaw.ai/gateway/security/exposure-runbook) và [hướng dẫn sandbox](https://docs.openclaw.ai/gateway/sandboxing).

## Tài liệu theo mục đích

| Bạn muốn làm gì? | Tài liệu nên xem |
| --- | --- |
| Cấu hình mô hình và xác thực | [Mô hình](https://docs.openclaw.ai/concepts/models) · [Nhà cung cấp mô hình](https://docs.openclaw.ai/concepts/model-providers) |
| Kết nối dịch vụ nhắn tin | [Các kênh](https://docs.openclaw.ai/channels) |
| Thêm công cụ, kỹ năng và plugin | [Công cụ](https://docs.openclaw.ai/tools) · [Kỹ năng](https://docs.openclaw.ai/tools/skills) · [Plugin](https://docs.openclaw.ai/plugins) · [ClawHub](https://clawhub.ai) |
| Chạy ứng dụng và nút thiết bị | [Nền tảng](https://docs.openclaw.ai/platforms) · [Nút thiết bị](https://docs.openclaw.ai/nodes) |
| Dùng CLI và lệnh trò chuyện | [Tài liệu CLI](https://docs.openclaw.ai/cli) · [Lệnh gạch chéo](https://docs.openclaw.ai/tools/slash-commands) |
| Cấu hình hoặc vận hành Gateway | [Cấu hình](https://docs.openclaw.ai/gateway/configuration) · [Kiến trúc](https://docs.openclaw.ai/concepts/architecture) · [Cập nhật](https://docs.openclaw.ai/install/updating) · [Kênh phát hành](https://docs.openclaw.ai/install/development-channels) |

## Phát triển

Kho mã nguồn này sử dụng pnpm workspace. Không hỗ trợ chạy `npm install` thông thường tại thư mục gốc.

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm build
pnpm ui:build
```

Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết quy trình đóng góp và [hướng dẫn thiết lập mã nguồn](https://docs.openclaw.ai/start/setup) để bắt đầu vòng lặp phát triển.

## Quản trị dự án

OpenClaw được phát triển công khai dưới sự quản lý của [OpenClaw Foundation](https://openclaw.org), một tổ chức độc lập theo diện 501(c)(3). Quỹ tuyển dụng nhóm nòng cốt và ký xác nhận các bản phát hành. Các nhà tài trợ và đơn vị hỗ trợ hạ tầng đóng góp cho quỹ nhưng không sở hữu hay chỉ đạo dự án. OpenAI là nhà tài trợ, không phải chủ sở hữu.

## Cộng đồng

Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết thông tin người duy trì dự án và hướng dẫn đóng góp. Các yêu cầu kéo (PR) có hỗ trợ AI cũng được hoan nghênh.

Hãy dùng [trang chọn loại vấn đề](https://github.com/openclaw/openclaw/issues/new/choose) để báo lỗi hoặc đề xuất tính năng; truy cập [cộng đồng OpenClaw chính thức](https://community.openclaw.ai/) để được hỗ trợ; và báo cáo lỗ hổng bảo mật qua [SECURITY.md](SECURITY.md). Những khả năng mới thường nên được phát triển thành plugin bằng [Plugin SDK](https://docs.openclaw.ai/plugins/building-plugins) và chia sẻ qua [ClawHub](https://clawhub.ai).

OpenClaw được Peter Steinberger và cộng đồng xây dựng cho **Molty**, một trợ lý AI hình tôm hùm không gian. Khám phá [lore của dự án](https://docs.openclaw.ai/start/lore), [soul.md](https://soul.md), [trang của Peter](https://steipete.me), [lịch sử sao](https://www.star-history.com/#openclaw/openclaw&type=date&legend=top-left) và [@openclaw](https://x.com/openclaw).

Xin cảm ơn đặc biệt [Mario Zechner](https://mariozechner.at/) vì sự hỗ trợ và dự án [pi](https://github.com/earendil-works/pi), cùng Adam Doppelt vì tên miền lobster.bot.

## Nhà tài trợ và đơn vị hỗ trợ

Quỹ nhận tài trợ từ Amazon, Lobster Computer Company, Offline Holdings, OpenAI, Red Hat và Đại học Michigan; hạ tầng được hỗ trợ bởi Blacksmith, Convex, GitHub, NVIDIA và Vercel.

<table>
  <tr>
    <td align="center"><a href="https://blacksmith.sh/"><picture><source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/blacksmith-light.svg"><img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/blacksmith.svg" alt="Blacksmith" height="28"></picture></a></td>
    <td align="center"><a href="https://www.convex.dev/"><picture><source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/convex-light.svg"><img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/convex.svg" alt="Convex" height="24"></picture></a></td>
    <td align="center"><a href="https://github.com/"><picture><source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/github-light.svg"><img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/github.svg" alt="GitHub" height="28"></picture></a></td>
    <td align="center"><a href="https://www.nvidia.com/"><picture><source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/nvidia.svg"><img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/nvidia-dark.svg" alt="NVIDIA" height="28"></picture></a></td>
    <td align="center"><a href="https://github.com/openai"><picture><source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/openai-light.svg"><img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/openai.svg" alt="OpenAI" height="28"></picture></a></td>
    <td align="center"><a href="https://github.com/redhat"><picture><source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/redhat-light.svg"><img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/redhat.svg" alt="Red Hat" height="28"></picture></a></td>
    <td align="center"><a href="https://vercel.com/"><picture><source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/vercel-light.svg"><img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/vercel.svg" alt="Vercel" height="24"></picture></a></td>
  </tr>
</table>

## Người đóng góp

Cảm ơn tất cả những người đã đóng góp cho OpenClaw! Xem danh sách người đóng góp tại [GitHub Contributors](https://github.com/openclaw/openclaw/graphs/contributors).

## Giấy phép

Dự án sử dụng [giấy phép MIT](LICENSE) © OpenClaw Foundation. Xem [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) để biết thông tin về mã nguồn bên thứ ba được tích hợp hoặc điều chỉnh.
