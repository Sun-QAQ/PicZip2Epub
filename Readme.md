### PicZip2Epub 项目文档

#### 项目简介
PicZip2Epub 是一个 Python 脚本，用于将包含图片的 ZIP 文件转换为 EPUB 格式电子书。该脚本可以读取 ZIP 文件中的所有图片文件，并将它们按顺序嵌入到一个 EPUB 文件中。

#### 安装依赖
在使用 PicZip2Epub 之前，请确保安装了以下依赖库：
- `ebooklib`：用于创建和操作 EPUB 文件。
- `zipfile`：Python 内置库，用于处理 ZIP 文件。

可以通过以下命令安装所需的第三方库：
```bash
pip install EbookLib
```

#### 使用方法
1. **准备ZIP文件**：确保你有一个包含图片的 ZIP 文件。
2. **修改脚本路径**：编辑 `main.py` 文件，将 `zip_path` 和 `output_epub` 变量设置为你自己的 ZIP 文件路径和输出 EPUB 文件名。
3. **运行脚本**：通过命令行运行脚本：
   ```bash
   python main.py
   ```

#### 代码说明
- **导入模块**：
  - `zipfile`：用于读取 ZIP 文件。
  - `ebooklib.epub`：用于创建 EPUB 文件。
  - `os`：用于操作系统相关功能（如果需要）。

- **函数定义**：
  - `create_epub_from_zip(zip_path, output_epub)`：主函数，负责从 ZIP 文件创建 EPUB 文件。
    - **参数**：
      - `zip_path`：输入 ZIP 文件的路径。
      - `output_epub`：输出 EPUB 文件的路径。
    - **步骤**：
      1. 打开并读取 ZIP 文件。
      2. 获取所有图片文件名并排序。
      3. 创建一个新的 EPUB 书籍对象。
      4. 设置书籍元数据（如标题、语言、作者等）。
      5. 将每张图片添加到 EPUB 中，并生成 HTML 章节内容。
      6. 创建章节以显示所有图片。
      7. 添加章节到书籍对象并设置目录。
      8. 写入最终的 EPUB 文件。

#### 注意事项
- 确保 ZIP 文件中只包含支持的图片格式（PNG、JPG、JPEG、GIF、BMP）。
- 如果 ZIP 文件较大或包含大量图片，生成 EPUB 文件可能需要一些时间。
- 输出的 EPUB 文件可以在大多数电子书阅读器上查看。

#### 示例
假设你有一个名为 `images.zip` 的 ZIP 文件，其中包含多张图片，并希望将其转换为名为 `output.epub` 的 EPUB 文件。你可以按照以下步骤操作：

1. 修改 `main.py` 文件中的路径：
   ```python
   zip_path = "path/to/images.zip"
   output_epub = "output.epub"
   ```
2. 运行脚本：
   ```bash
   python main.py
   ```

#### 未来改进
- 支持更多图片格式。
- 增加命令行参数以动态指定输入和输出文件路径。
- 提供用户界面以简化操作流程。
- 支持多线程或异步处理以提高性能。

---

以上是 PicZip2Epub 项目的详细文档，希望对你有所帮助！如果有任何问题或建议，请随时提出。