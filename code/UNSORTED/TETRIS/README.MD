## משחק מס' 2: טטריס

### תיאור

משחק פאזל קלאסי שבו צורות (טטרומינו) נופלות מלמעלה, והשחקן נדרש לסובב ולהזיז אותן כדי ליצור קווים אופקיים מלאים.

### כללים

1.  צורות הטטרומינו נופלות מחלקו העליון של לוח המשחק.
2.  השחקן רשאי לסובב ולהזיז את הצורות הנופלות.
3.  כאשר שורה אופקית מתמלאת, היא נעלמת והשחקן מקבל נקודות.
4.  המשחק מסתיים אם לא ניתן להכניס צורות חדשות ללוח.

### קוד

```python
import sys, random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor

class Tetris(QMainWindow):
    """
    החלון הראשי של יישום טטריס.
    """
    def __init__(self) -> None:
        """
        אתחול חלון הטטריס.
        """
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        """
         אתחול ממשק המשתמש.
        """
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)
        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        self.tboard.start()
        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self) -> None:
        """
        מרכז את החלון על המסך.
        """
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


class Board(QFrame):
    """
    מחלקה המייצגת את לוח המשחק של טטריס.
    """
    msg2Statusbar = pyqtSignal(str)
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent: QMainWindow) -> None:
        """
        אתחול לוח המשחק.
        
        Args:
            parent: חלון האב.
        """
        super().__init__(parent)
        self.initBoard()

    def initBoard(self) -> None:
         """
        מאתחל את הלוח ואת משתני המשחק.
        """
        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False
        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []
        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()

    def shapeAt(self, x: int, y: int) -> int:
        """
        מחזיר את צורת הטטרומינו במיקום הנתון.
        
        Args:
            x: קואורדינטת x.
            y: קואורדינטת y.
        Returns:
            צורת הטטרומינו במיקום.
        """
        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x: int, y: int, shape: int) -> None:
        """
        קובע את צורת הטטרומינו במיקום הנתון.
        
        Args:
            x: קואורדינטת x.
            y: קואורדינטת y.
            shape: צורת הטטרומינו.
        """
        self.board[(y * Board.BoardWidth) + x] = shape

    def squareWidth(self) -> int:
         """
        מחזיר את רוחב ריבוע בודד.
        
        Returns:
             רוחב הריבוע.
        """
        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self) -> int:
        """
        מחזיר את גובה ריבוע בודד.
         
        Returns:
             גובה הריבוע.
        """
        return self.contentsRect().height() // Board.BoardHeight

    def start(self) -> None:
         """
        מפעיל את המשחק.
        """
        if self.isPaused:
            return
        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()
        self.msg2Statusbar.emit(str(self.numLinesRemoved))
        self.newPiece()
        self.timer.start(Board.Speed, self)

    def pause(self) -> None:
         """
        משהה או מחדש את המשחק.
        """
        if not self.isStarted:
            return
        self.isPaused = not self.isPaused
        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")
        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))
        self.update()

    def paintEvent(self, event: object) -> None:
          """
         מצייר את לוח המשחק ואת הצורה הנוכחית.
         
         Args:
             event: אירוע הציור.
         """
        painter = QPainter(self)
        rect = self.contentsRect()
        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)
                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                        rect.left() + j * self.squareWidth(),
                        boardTop + i * self.squareHeight(), shape)
        if self.curPiece.shape() != Tetrominoe.NoShape:
            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                    boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                    self.curPiece.shape())

    def keyPressEvent(self, event: object) -> None:
        """
        מטפל בלחיצות מקשים.
         
        Args:
             event: אירוע לחיצת מקש.
        """
        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return
        key = event.key()
        if key == Qt.Key_P:
            self.pause()
            return
        if self.isPaused:
            return
        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
        elif key == Qt.Key_Space:
            self.dropDown()
        elif key == Qt.Key_D:
            self.oneLineDown()
        else:
            super(Board, self).keyPressEvent(event)

    def timerEvent(self, event: object) -> None:
          """
         מטפל באירועי הטיימר.
         
         Args:
            event: אירוע הטיימר.
        """
        if event.timerId() == self.timer.timerId():
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()
        else:
            super(Board, self).timerEvent(event)

    def clearBoard(self) -> None:
        """
        מנקה את לוח המשחק.
        """
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

    def dropDown(self) -> None:
         """
        מוריד את הצורה הנוכחית עד למטה.
        """
        newY = self.curY
        while newY > 0:
            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break
            newY -= 1
        self.pieceDropped()

    def oneLineDown(self) -> None:
         """
        מוריד את הצורה הנוכחית בשורה אחת.
        """
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()

    def pieceDropped(self) -> None:
        """
        מקבע את הצורה שנפלה על הלוח.
        """
        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())
        self.removeFullLines()
        if not self.isWaitingAfterLine:
            self.newPiece()

    def removeFullLines(self) -> None:
        """
        מסיר שורות מלאות ומעדכן את מונה הנקודות.
        """
        numFullLines = 0
        rowsToRemove = []
        for i in range(Board.BoardHeight):
            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1
            if n == 10:
                rowsToRemove.append(i)
        rowsToRemove.reverse()
        for m in rowsToRemove:
            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                        self.setShapeAt(l, k, self.shapeAt(l, k + 1))
        numFullLines = numFullLines + len(rowsToRemove)
        if numFullLines > 0:
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))
            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()

    def newPiece(self) -> None:
         """
        מייצר צורה חדשה למשחק.
        """
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()
        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")

    def tryMove(self, newPiece: object, newX: int, newY: int) -> bool:
         """
        מנסה להזיז את הצורה לקואורדינטות חדשות.
        
        Args:
            newPiece: צורת הטטרומינו החדשה.
            newX: קואורדינטת X חדשה.
            newY: קואורדינטת Y חדשה.
        
        Returns:
            True אם ההזזה הצליחה, אחרת False.
        """
        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False
            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False
        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()
        return True

    def drawSquare(self, painter: QPainter, x: int, y: int, shape: int) -> None:
         """
        מצייר ריבוע על לוח המשחק.
        
         Args:
             painter: אובייקט QPainter.
             x: קואורדינטת x.
             y: קואורדינטת y.
             shape: צורת הטטרומינו.
        """
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
            self.squareHeight() - 2, color)
        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)
        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class Tetrominoe(object):
    """
    מנייה של כל צורות הטטרומינו האפשריות.
    """
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7

class Shape(object):
    """
    מחלקה המייצגת צורת טטרומינו.
    """
    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )
    def __init__(self) -> None:
        """
         אתחול צורת הטטרומינו.
        """
        self.coords = [[0, 0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape
        self.setShape(Tetrominoe.NoShape)

    def shape(self) -> int:
        """
        מחזיר את צורת הטטרומינו.
        
        Returns:
             צורת הטטרומינו.
        """
        return self.pieceShape

    def setShape(self, shape: int) -> None:
        """
        קובע את צורת הטטרומינו.
        
        Args:
            shape: צורת הטטרומינו.
        """
        table = Shape.coordsTable[shape]
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]
        self.pieceShape = shape

    def setRandomShape(self) -> None:
        """
        קובע צורת טטרומינו אקראית.
        """
        self.setShape(random.randint(1, 7))

    def x(self, index: int) -> int:
         """
        מחזיר את קואורדינטת x עבור נקודה נתונה של הצורה.
        
        Args:
            index: אינדקס נקודת הצורה.
        Returns:
            קואורדינטת x.
        """
        return self.coords[index][0]

    def y(self, index: int) -> int:
         """
        מחזיר את קואורדינטת y עבור נקודה נתונה של הצורה.
        
        Args:
            index: אינדקס נקודת הצורה.
        Returns:
             קואורדינטת y.
        """
        return self.coords[index][1]

    def setX(self, index: int, x: int) -> None:
          """
         קובע את קואורדינטת x עבור נקודה נתונה של הצורה.
         
        Args:
             index: אינדקס נקודת הצורה.
             x: קואורדינטת x החדשה.
        """
        self.coords[index][0] = x

    def setY(self, index: int, y: int) -> None:
         """
        קובע את קואורדינטת y עבור נקודה נתונה של הצורה.
        
        Args:
            index: אינדקס נקודת הצורה.
            y: קואורדינטת y החדשה.
        """
        self.coords[index][1] = y

    def minX(self) -> int:
        """
         מחזיר את קואורדינטת x המינימלית עבור הצורה.
        
        Returns:
             קואורדינטת x המינימלית.
        """
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])
        return m

    def maxX(self) -> int:
          """
         מחזיר את קואורדינטת x המקסימלית עבור הצורה.
         
        Returns:
             קואורדינטת x המקסימלית.
        """
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])
        return m

    def minY(self) -> int:
         """
         מחזיר את קואורדינטת y המינימלית עבור הצורה.
        
         Returns:
             קואורדינטת y המינימלית.
        """
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])
        return m

    def maxY(self) -> int:
        """
        מחזיר את קואורדינטת y המקסימלית עבור הצורה.
       
        Returns:
             קואורדינטת y המקסימלית.
        """
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])
        return m

    def rotateLeft(self) -> object:
         """
        מסובב את הצורה ב-90 מעלות שמאלה.
        
        Returns:
            צורת הטטרומינו החדשה לאחר הסיבוב.
        """
        if self.pieceShape == Tetrominoe.SquareShape:
            return self
        result = Shape()
        result.pieceShape = self.pieceShape
        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))
        return result

    def rotateRight(self) -> object:
        """
        מסובב את הצורה ב-90 מעלות ימינה.
        
        Returns:
            צורת הטטרומינו החדשה לאחר הסיבוב.
        """
        if self.pieceShape == Tetrominoe.SquareShape:
            return self
        result = Shape()
        result.pieceShape = self.pieceShape
        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))
        return result

if __name__ == '__main__':
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())
```

### ניתוח קוד

*   **מחלקה `Tetris`:**
    *   יוצרת את החלון הראשי של היישום.
    *   `initUI()`: מאתחלת את הממשק, יוצרת את לוח המשחק.
*   **מחלקה `Board`:**
    *   `initBoard()`: מאתחלת את לוח המשחק, הטיימר והצורה הנוכחית.
    *   `start()`: מפעילה את המשחק, מייצרת צורה חדשה.
    *   `pause()`: משהה את המשחק.
    *   `paintEvent()`: מציירת את לוח המשחק ואת הצורה הנופלת.
    *   `keyPressEvent()`: מטפלת בלחיצות מקשים.
    *   `timerEvent()`: מפעילה את שיטת `oneLineDown` לפי הטיימר.
    *   `clearBoard()`: מנקה את לוח המשחק.
    *   `dropDown()`: מורידה את הצורה עד למטה.
    *   `oneLineDown()`: מורידה את הצורה בשורה אחת.
    *   `pieceDropped()`: מקבעת את הצורה על הלוח.
    *   `removeFullLines()`: מסירה שורות מלאות.
    *   `newPiece()`: יוצרת צורה חדשה.
    *   `tryMove()`: מנסה להזיז את הצורה.
    *   `drawSquare()`: מציירת ריבוע אחד.
*   **מחלקה `Tetrominoe`:**
    *   מגדירה את כל צורות הטטרומינו האפשריות.
*   **מחלקה `Shape`:**
    *   מייצגת צורת טטרומינו בודדת.
    *   `setShape()`: קובעת את צורת הטטרומינו.
    *   `setRandomShape()`: בוחרת צורת טטרומינו אקראית.
    *   `x()`/`y()`: מחזירות את קואורדינטות הטטרומינו.
    *   `rotateLeft()`/`rotateRight()`: מסובבות את צורת הטטרומינו.

### דיאגרמת זרימה
```mermaid
graph TD
    A[Начало игры] --> B{Игра запущена?};
    B -- Да --> C{Пауза?};
    C -- Да --> D[Остановить таймер];
    D --> E[Ожидание];
    C -- Нет --> F[Обработка нажатия клавиши];
    F --> G[Движение/поворот фигуры];
    G --> H{Таймер?};
     H -- Да --> I[Опустить фигуру на 1 линию];
     I --> J[Обработка столкновения с низом или другой фигурой];
     J --> K{Есть полная линия?};
     K -- Да --> L[Удалить полные линии];
      L --> M[Создать новую фигуру];
      K -- Нет --> M;
       H -- Нет -->M;
      M --> B;
    B -- Нет --> N[Конец игры];
    N --> O[Завершение];
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style N fill:#f9f,stroke:#333,stroke-width:2px
```