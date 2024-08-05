
# CMPSC 104 - Document Engineering Lab 2 Assignment: reStructuredText

## Name
[Your Name Here]

## GitHub Account Name
[Your GitHub Name Here]

---

## Text Emphasis
1. Provide an example of **bold text** and *italic text* using reStructuredText.
   ```rst
   **bold text**
   *italic text*
   ```

## Titles/Headings
2. Create a document with the following structure using reStructuredText:
   - Title
   - Section
   - Subsection
   ```rst
   ================
   Title
   ================

   Section
   ---------------

   Subsection
   ^^^^^^^^^^^^^^^^
   ```

## Links
3. Write a reStructuredText example that includes an inline link and a reference link.
   ```rst
   `Inline Link <http://example.com>`_

   .. _reference link:

   `Reference Link`_
   ```

## Literal or Code Blocks
4. Provide an example of a code block in reStructuredText.
   ```rst
   .. code:: python

      def hello_world():
          print("Hello, world!")
   ```

## Lists
5. Create an ordered list and an unordered list using reStructuredText.
   ```rst
   1. First item
   2. Second item
   3. Third item

   - Bullet item 1
   - Bullet item 2
   - Bullet item 3
   ```

## Documentation Comments
6. Add a comment in reStructuredText that will not be rendered in the final document.
   ```rst
   .. This is a comment and will not be rendered.
   ```

## Admonition
7. Write examples of the following admonitions in reStructuredText:
   - .. note::
   - .. danger::
   ```rst
   .. note::
      This is a note admonition.

   .. danger::
      This is a danger admonition.
   ```

## Tables
8. Create a simple table in reStructuredText.
   ```rst
   =====  =======
   Item   Quantity
   =====  =======
   Apples 5
   Oranges 3
   =====  =======
   ```

## Rendering Image
9. Include an image in a reStructuredText document.
   ```rst
   .. image:: path/to/image.png
      :alt: Image description
   ```

## Directives
10. Write an example of using a directive in reStructuredText, such as including content from another file.
   ```rst
   .. include:: another_file.rst
   ```