# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(938, 652)
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks|QMainWindow.DockOption.ForceTabbedDocks)
        self.actionOKX = QAction(MainWindow)
        self.actionOKX.setObjectName(u"actionOKX")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertLink))
        self.actionOKX.setIcon(icon)
        self.action_start = QAction(MainWindow)
        self.action_start.setObjectName(u"action_start")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.action_start.setIcon(icon1)
        self.action_stop = QAction(MainWindow)
        self.action_stop.setObjectName(u"action_stop")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.action_stop.setIcon(icon2)
        self.action_stop.setMenuRole(QAction.MenuRole.NoRole)
        self.action_back = QAction(MainWindow)
        self.action_back.setObjectName(u"action_back")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekBackward))
        self.action_back.setIcon(icon3)
        self.action_back.setMenuRole(QAction.MenuRole.NoRole)
        self.action_forward = QAction(MainWindow)
        self.action_forward.setObjectName(u"action_forward")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekForward))
        self.action_forward.setIcon(icon4)
        self.action_forward.setMenuRole(QAction.MenuRole.NoRole)
        self.action_skip = QAction(MainWindow)
        self.action_skip.setObjectName(u"action_skip")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward))
        self.action_skip.setIcon(icon5)
        self.action_skip.setMenuRole(QAction.MenuRole.NoRole)
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.action_open.setIcon(icon6)
        self.action_open.setMenuRole(QAction.MenuRole.NoRole)
        self.action_config = QAction(MainWindow)
        self.action_config.setObjectName(u"action_config")
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.action_config.setIcon(icon7)
        self.action_config.setMenuRole(QAction.MenuRole.NoRole)
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SyncSynchronizing))
        self.action_clear.setIcon(icon8)
        self.actionBinance = QAction(MainWindow)
        self.actionBinance.setObjectName(u"actionBinance")
        self.actionBinance.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, -1, -1, 0)
        self.k_chart = QChartView(self.centralwidget)
        self.k_chart.setObjectName(u"k_chart")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.k_chart.sizePolicy().hasHeightForWidth())
        self.k_chart.setSizePolicy(sizePolicy)
        self.k_chart.setMinimumSize(QSize(0, 180))

        self.gridLayout.addWidget(self.k_chart, 0, 0, 1, 2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.formLayout_2.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.formLayout_2.setHorizontalSpacing(-1)
        self.formLayout_2.setVerticalSpacing(-1)
        self.formLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.symbol_combo_box = QComboBox(self.centralwidget)
        self.symbol_combo_box.setObjectName(u"symbol_combo_box")
        self.symbol_combo_box.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.symbol_combo_box)

        self.interval_combo_box = QComboBox(self.centralwidget)
        self.interval_combo_box.addItem("")
        self.interval_combo_box.addItem("")
        self.interval_combo_box.addItem("")
        self.interval_combo_box.addItem("")
        self.interval_combo_box.setObjectName(u"interval_combo_box")
        self.interval_combo_box.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.interval_combo_box)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dateEdit_2 = QDateEdit(self.centralwidget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.horizontalLayout.addWidget(self.dateEdit_2)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout.addWidget(self.dateEdit)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.comboBox_4 = QComboBox(self.centralwidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(150, 0))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comboBox_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(120, 0))
        self.doubleSpinBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_3.addWidget(self.comboBox_3)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignRight)


        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)

        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.gridLayout_2)


        self.gridLayout.addLayout(self.formLayout_2, 1, 0, 1, 1)

        self.volume_chart = QChartView(self.centralwidget)
        self.volume_chart.setObjectName(u"volume_chart")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.volume_chart.sizePolicy().hasHeightForWidth())
        self.volume_chart.setSizePolicy(sizePolicy1)
        self.volume_chart.setMinimumSize(QSize(0, 0))
        self.volume_chart.setInteractive(True)

        self.gridLayout.addWidget(self.volume_chart, 1, 1, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setSizeIncrement(QSize(0, 0))
        self.tabWidget.setToolTipDuration(-1)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(0, 26))
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget_3 = QTableWidget(self.tab)
        if (self.tableWidget_3.rowCount() < 15):
            self.tableWidget_3.setRowCount(15)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        sizePolicy.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy)
        self.tableWidget_3.setAcceptDrops(False)
        self.tableWidget_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableWidget_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.tableWidget_3.setLineWidth(1)
        self.tableWidget_3.setRowCount(15)
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_2.addWidget(self.tableWidget_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_log = QWidget()
        self.tab_log.setObjectName(u"tab_log")
        self.verticalLayout_3 = QVBoxLayout(self.tab_log)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.log_text = QTextEdit(self.tab_log)
        self.log_text.setObjectName(u"log_text")
        self.log_text.setReadOnly(True)
        self.log_text.setOverwriteMode(True)

        self.verticalLayout_3.addWidget(self.log_text)

        self.log_widget = QTableWidget(self.tab_log)
        if (self.log_widget.rowCount() < 15):
            self.log_widget.setRowCount(15)
        self.log_widget.setObjectName(u"log_widget")
        sizePolicy.setHeightForWidth(self.log_widget.sizePolicy().hasHeightForWidth())
        self.log_widget.setSizePolicy(sizePolicy)
        self.log_widget.setAcceptDrops(False)
        self.log_widget.setFrameShape(QFrame.Shape.StyledPanel)
        self.log_widget.setFrameShadow(QFrame.Shadow.Sunken)
        self.log_widget.setLineWidth(1)
        self.log_widget.setRowCount(15)
        self.log_widget.setColumnCount(0)
        self.log_widget.horizontalHeader().setVisible(False)
        self.log_widget.horizontalHeader().setCascadingSectionResizes(True)
        self.log_widget.horizontalHeader().setHighlightSections(True)
        self.log_widget.horizontalHeader().setStretchLastSection(True)
        self.log_widget.verticalHeader().setVisible(False)
        self.log_widget.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_3.addWidget(self.log_widget)

        self.tabWidget.addTab(self.tab_log, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 2)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setColumnStretch(0, 1)

        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 938, 24))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setEnabled(True)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        QWidget.setTabOrder(self.volume_chart, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.dateEdit_2)
        QWidget.setTabOrder(self.dateEdit_2, self.symbol_combo_box)
        QWidget.setTabOrder(self.symbol_combo_box, self.interval_combo_box)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionOKX)
        self.menu.addAction(self.actionBinance)
        self.menu_2.addAction(self.action_clear)
        self.toolBar.addAction(self.action_open)
        self.toolBar.addAction(self.action_config)
        self.toolBar.addAction(self.action_start)
        self.toolBar.addAction(self.action_stop)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOKX.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5OKX", None))
        self.action_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
#if QT_CONFIG(tooltip)
        self.action_start.setToolTip(QCoreApplication.translate("MainWindow", u" \u5f00\u59cb", None))
#endif // QT_CONFIG(tooltip)
        self.action_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
#if QT_CONFIG(tooltip)
        self.action_stop.setToolTip(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
#endif // QT_CONFIG(tooltip)
        self.action_back.setText(QCoreApplication.translate("MainWindow", u"\u540e\u9000", None))
#if QT_CONFIG(tooltip)
        self.action_back.setToolTip(QCoreApplication.translate("MainWindow", u"\u540e\u9000", None))
#endif // QT_CONFIG(tooltip)
        self.action_forward.setText(QCoreApplication.translate("MainWindow", u"\u524d\u8fdb", None))
#if QT_CONFIG(tooltip)
        self.action_forward.setToolTip(QCoreApplication.translate("MainWindow", u"\u524d\u8fdb", None))
#endif // QT_CONFIG(tooltip)
        self.action_skip.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8fc7", None))
#if QT_CONFIG(tooltip)
        self.action_skip.setToolTip(QCoreApplication.translate("MainWindow", u"\u8df3\u8fc7", None))
#endif // QT_CONFIG(tooltip)
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(tooltip)
        self.action_open.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#endif // QT_CONFIG(tooltip)
        self.action_config.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.action_config.setToolTip(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7406\u6570\u636e", None))
#if QT_CONFIG(tooltip)
        self.action_clear.setToolTip(QCoreApplication.translate("MainWindow", u"\u6e05\u7406\u6570\u636e", None))
#endif // QT_CONFIG(tooltip)
        self.actionBinance.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u5e01\u5b89", None))
#if QT_CONFIG(tooltip)
        self.actionBinance.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u5e01\u5b89", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u54c1\u79cd", None))
        self.interval_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"15\u5206", None))
        self.interval_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"1\u5c0f\u65f6", None))
        self.interval_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"4\u5c0f\u65f6", None))
        self.interval_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"1\u65e5", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy.MM.dd", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy.MM.dd", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u65f6", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"\u96f6\u5ef6\u65f6\uff0c\u7406\u60f3\u6267\u884c", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5165\u91d1", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"1x", u"1x"))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"3x", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"5x", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"10x", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"20x", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"30x", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"50x", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"75x", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"100x", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6760\u6746", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u4f18\u5316", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u7b56\u7565\u91cd\u8f7d", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u4ea4\u6613", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_log), QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

