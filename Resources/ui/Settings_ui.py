# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsFWYbnt.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QCheckBox,
    QFrame,
    QGridLayout,
    QGroupBox,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QSpinBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.setWindowModality(Qt.WindowModality.WindowModal)
        Form.resize(580, 724)
        Form.setAutoFillBackground(False)
        self.gridLayout_7 = QGridLayout(Form)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.Cancel = QPushButton(Form)
        self.Cancel.setObjectName("Cancel")

        self.gridLayout_6.addWidget(self.Cancel, 0, 1, 1, 1)

        self.GenerateJsonExit = QPushButton(Form)
        self.GenerateJsonExit.setObjectName("GenerateJsonExit")

        self.gridLayout_6.addWidget(self.GenerateJsonExit, 0, 2, 1, 1)

        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideRight)
        self.General = QWidget()
        self.General.setObjectName("General")
        self.General.setEnabled(True)
        self.General.setAutoFillBackground(True)
        self.gridLayout_9 = QGridLayout(self.General)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DebugMode = QCheckBox(self.General)
        self.DebugMode.setObjectName("DebugMode")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DebugMode.sizePolicy().hasHeightForWidth())
        self.DebugMode.setSizePolicy(sizePolicy)
        self.DebugMode.setMinimumSize(QSize(0, 0))
        self.DebugMode.setMaximumSize(QSize(150, 16777215))
        self.DebugMode.setBaseSize(QSize(20, 0))

        self.verticalLayout_2.addWidget(self.DebugMode)

        self.label_3 = QLabel(self.General)
        self.label_3.setObjectName("label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(300, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.gridLayout_9.addLayout(self.verticalLayout_2, 6, 0, 1, 1)

        self.groupBox = QGroupBox(self.General)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setMinimumSize(QSize(0, 300))
        font = QFont()
        font.setBold(True)
        self.groupBox.setFont(font)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        font1 = QFont()
        font1.setBold(False)
        self.groupBox_3.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ShowText_Small = QCheckBox(self.groupBox_3)
        self.ShowText_Small.setObjectName("ShowText_Small")
        self.ShowText_Small.setFont(font1)

        self.verticalLayout.addWidget(self.ShowText_Small)

        self.ShowText_Medium = QCheckBox(self.groupBox_3)
        self.ShowText_Medium.setObjectName("ShowText_Medium")
        self.ShowText_Medium.setFont(font1)

        self.verticalLayout.addWidget(self.ShowText_Medium)

        self.ShowText_Large = QCheckBox(self.groupBox_3)
        self.ShowText_Large.setObjectName("ShowText_Large")
        self.ShowText_Large.setFont(font1)

        self.verticalLayout.addWidget(self.ShowText_Large)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setFont(font1)
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.IconSize_Small = QSpinBox(self.groupBox_4)
        self.IconSize_Small.setObjectName("IconSize_Small")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.IconSize_Small.sizePolicy().hasHeightForWidth())
        self.IconSize_Small.setSizePolicy(sizePolicy2)
        self.IconSize_Small.setMinimumSize(QSize(50, 0))
        self.IconSize_Small.setSizeIncrement(QSize(0, 0))
        self.IconSize_Small.setBaseSize(QSize(0, 0))
        self.IconSize_Small.setFont(font1)
        self.IconSize_Small.setFrame(True)
        self.IconSize_Small.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.IconSize_Small.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.IconSize_Small.setProperty("showGroupSeparator", False)
        self.IconSize_Small.setMinimum(0)
        self.IconSize_Small.setValue(24)

        self.gridLayout.addWidget(self.IconSize_Small, 0, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName("label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(130, 0))
        self.label_11.setFont(font1)

        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)

        self.IconSize_Medium = QSpinBox(self.groupBox_4)
        self.IconSize_Medium.setObjectName("IconSize_Medium")
        sizePolicy2.setHeightForWidth(self.IconSize_Medium.sizePolicy().hasHeightForWidth())
        self.IconSize_Medium.setSizePolicy(sizePolicy2)
        self.IconSize_Medium.setMinimumSize(QSize(50, 0))
        self.IconSize_Medium.setBaseSize(QSize(0, 0))
        self.IconSize_Medium.setFont(font1)
        self.IconSize_Medium.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.IconSize_Medium.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.IconSize_Medium.setValue(44)

        self.gridLayout.addWidget(self.IconSize_Medium, 1, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(130, 0))
        self.label_10.setFont(font1)

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName("groupBox_5")
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.groupBox_5.setFont(font1)
        self.gridLayout_11 = QGridLayout(self.groupBox_5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.MaxPanelColumn = QSpinBox(self.groupBox_5)
        self.MaxPanelColumn.setObjectName("MaxPanelColumn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MaxPanelColumn.sizePolicy().hasHeightForWidth())
        self.MaxPanelColumn.setSizePolicy(sizePolicy3)
        self.MaxPanelColumn.setMinimumSize(QSize(50, 0))
        self.MaxPanelColumn.setMinimum(0)
        self.MaxPanelColumn.setMaximum(99)
        self.MaxPanelColumn.setValue(6)

        self.gridLayout_10.addWidget(self.MaxPanelColumn, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox_5)
        self.label.setObjectName("label")

        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName("label_2")
        self.label_2.setMinimumSize(QSize(0, 10))

        self.gridLayout_10.addWidget(self.label_2, 1, 0, 1, 3)

        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox_5, 2, 0, 1, 1)

        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.groupBox_2.setMinimumSize(QSize(0, 60))
        self.groupBox_2.setFont(font1)
        self.gridLayout_12 = QGridLayout(self.groupBox_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, 9, -1, -1)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.label_7.setFrameShape(QFrame.Shape.Box)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout_12.addWidget(self.label_7, 0, 0, 1, 1)

        self.StyleSheetLocation = QPushButton(self.groupBox_2)
        self.StyleSheetLocation.setObjectName("StyleSheetLocation")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(20)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.StyleSheetLocation.sizePolicy().hasHeightForWidth())
        self.StyleSheetLocation.setSizePolicy(sizePolicy5)
        self.StyleSheetLocation.setMinimumSize(QSize(20, 0))

        self.gridLayout_12.addWidget(self.StyleSheetLocation, 0, 1, 1, 1)

        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.gridLayout_9.addWidget(self.groupBox, 2, 0, 1, 1)

        self.groupBox1 = QGroupBox(self.General)
        self.groupBox1.setObjectName("groupBox1")
        self.groupBox1.setMinimumSize(QSize(0, 120))
        self.groupBox1.setFont(font)
        self.gridLayout_8 = QGridLayout(self.groupBox1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_8.setContentsMargins(6, 6, 6, 6)
        self.EnableBackup = QCheckBox(self.groupBox1)
        self.EnableBackup.setObjectName("EnableBackup")
        self.EnableBackup.setFont(font1)

        self.gridLayout_8.addWidget(self.EnableBackup, 0, 0, 1, 1)

        self.groupBox_Backup = QGroupBox(self.groupBox1)
        self.groupBox_Backup.setObjectName("groupBox_Backup")
        self.groupBox_Backup.setEnabled(False)
        sizePolicy.setHeightForWidth(self.groupBox_Backup.sizePolicy().hasHeightForWidth())
        self.groupBox_Backup.setSizePolicy(sizePolicy)
        self.groupBox_Backup.setMinimumSize(QSize(0, 50))
        self.groupBox_Backup.setFont(font1)
        self.gridLayout_13 = QGridLayout(self.groupBox_Backup)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_4 = QLabel(self.groupBox_Backup)
        self.label_4.setObjectName("label_4")
        self.label_4.setFrameShape(QFrame.Shape.Box)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )

        self.gridLayout_13.addWidget(self.label_4, 0, 0, 1, 1)

        self.BackUpLocation = QPushButton(self.groupBox_Backup)
        self.BackUpLocation.setObjectName("BackUpLocation")
        sizePolicy5.setHeightForWidth(self.BackUpLocation.sizePolicy().hasHeightForWidth())
        self.BackUpLocation.setSizePolicy(sizePolicy5)
        self.BackUpLocation.setMinimumSize(QSize(20, 0))

        self.gridLayout_13.addWidget(self.BackUpLocation, 0, 1, 1, 1)

        self.gridLayout_8.addWidget(self.groupBox_Backup, 1, 0, 1, 1)

        self.gridLayout_9.addWidget(self.groupBox1, 0, 0, 2, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_7, 5, 0, 1, 1)

        self.tabWidget.addTab(self.General, "")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_14 = QGridLayout(self.tab)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_18 = QGridLayout(self.groupBox_7)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.ScrollClicks_TabBar = QSpinBox(self.groupBox_7)
        self.ScrollClicks_TabBar.setObjectName("ScrollClicks_TabBar")
        sizePolicy2.setHeightForWidth(self.ScrollClicks_TabBar.sizePolicy().hasHeightForWidth())
        self.ScrollClicks_TabBar.setSizePolicy(sizePolicy2)
        self.ScrollClicks_TabBar.setMinimumSize(QSize(50, 0))
        self.ScrollClicks_TabBar.setSizeIncrement(QSize(0, 0))
        self.ScrollClicks_TabBar.setBaseSize(QSize(0, 0))
        self.ScrollClicks_TabBar.setFont(font1)
        self.ScrollClicks_TabBar.setFrame(True)
        self.ScrollClicks_TabBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ScrollClicks_TabBar.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.ScrollClicks_TabBar.setProperty("showGroupSeparator", False)
        self.ScrollClicks_TabBar.setMinimum(0)
        self.ScrollClicks_TabBar.setMaximum(10)
        self.ScrollClicks_TabBar.setValue(1)
        self.ScrollClicks_TabBar.setDisplayIntegerBase(10)

        self.gridLayout_17.addWidget(self.ScrollClicks_TabBar, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName("label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMinimumSize(QSize(130, 0))
        self.label_14.setFont(font1)

        self.gridLayout_17.addWidget(self.label_14, 1, 0, 1, 1)

        self.ScrollClicks_Ribbon = QSpinBox(self.groupBox_7)
        self.ScrollClicks_Ribbon.setObjectName("ScrollClicks_Ribbon")
        sizePolicy2.setHeightForWidth(self.ScrollClicks_Ribbon.sizePolicy().hasHeightForWidth())
        self.ScrollClicks_Ribbon.setSizePolicy(sizePolicy2)
        self.ScrollClicks_Ribbon.setMinimumSize(QSize(50, 0))
        self.ScrollClicks_Ribbon.setBaseSize(QSize(0, 0))
        self.ScrollClicks_Ribbon.setFont(font1)
        self.ScrollClicks_Ribbon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ScrollClicks_Ribbon.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.ScrollClicks_Ribbon.setMaximum(10)
        self.ScrollClicks_Ribbon.setValue(1)
        self.ScrollClicks_Ribbon.setDisplayIntegerBase(10)

        self.gridLayout_17.addWidget(self.ScrollClicks_Ribbon, 1, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName("label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMinimumSize(QSize(130, 0))
        self.label_15.setFont(font1)

        self.gridLayout_17.addWidget(self.label_15, 0, 0, 1, 1)

        self.gridLayout_18.addLayout(self.gridLayout_17, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.gridLayout_14.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_16 = QGridLayout(self.groupBox_6)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.EnableEnterEvent = QCheckBox(self.groupBox_6)
        self.EnableEnterEvent.setObjectName("EnableEnterEvent")

        self.gridLayout_15.addWidget(self.EnableEnterEvent, 0, 0, 1, 1)

        self.ScrollSpeed_Ribbon = QSlider(self.groupBox_6)
        self.ScrollSpeed_Ribbon.setObjectName("ScrollSpeed_Ribbon")
        self.ScrollSpeed_Ribbon.setMaximum(10)
        self.ScrollSpeed_Ribbon.setPageStep(1)
        self.ScrollSpeed_Ribbon.setValue(5)
        self.ScrollSpeed_Ribbon.setOrientation(Qt.Orientation.Horizontal)
        self.ScrollSpeed_Ribbon.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.ScrollSpeed_Ribbon.setTickInterval(1)

        self.gridLayout_15.addWidget(self.ScrollSpeed_Ribbon, 2, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName("label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(130, 0))
        self.label_12.setFont(font1)

        self.gridLayout_15.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_6)
        self.label_13.setObjectName("label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMinimumSize(QSize(130, 0))
        self.label_13.setFont(font1)

        self.gridLayout_15.addWidget(self.label_13, 1, 0, 1, 1)

        self.ScrollSpeed_TabBar = QSlider(self.groupBox_6)
        self.ScrollSpeed_TabBar.setObjectName("ScrollSpeed_TabBar")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.ScrollSpeed_TabBar.sizePolicy().hasHeightForWidth())
        self.ScrollSpeed_TabBar.setSizePolicy(sizePolicy6)
        self.ScrollSpeed_TabBar.setMaximum(10)
        self.ScrollSpeed_TabBar.setSingleStep(1)
        self.ScrollSpeed_TabBar.setPageStep(1)
        self.ScrollSpeed_TabBar.setValue(5)
        self.ScrollSpeed_TabBar.setSliderPosition(5)
        self.ScrollSpeed_TabBar.setOrientation(Qt.Orientation.Horizontal)
        self.ScrollSpeed_TabBar.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.ScrollSpeed_TabBar.setTickInterval(1)

        self.gridLayout_15.addWidget(self.ScrollSpeed_TabBar, 1, 1, 1, 1)

        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        self.gridLayout_14.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_19 = QGridLayout(self.tab_2)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.groupBox_9 = QGroupBox(self.tab_2)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_23 = QGridLayout(self.groupBox_9)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_6, 1, 1, 1, 1)

        self.CustomIcons = QCheckBox(self.groupBox_9)
        self.CustomIcons.setObjectName("CustomIcons")

        self.gridLayout_23.addWidget(self.CustomIcons, 0, 0, 1, 1)

        self.IconS = QGroupBox(self.groupBox_9)
        self.IconS.setObjectName("IconS")
        self.IconS.setEnabled(False)
        self.gridLayout_22 = QGridLayout(self.IconS)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.Tab_Scroll_Left = QPushButton(self.IconS)
        self.Tab_Scroll_Left.setObjectName("Tab_Scroll_Left")
        sizePolicy3.setHeightForWidth(self.Tab_Scroll_Left.sizePolicy().hasHeightForWidth())
        self.Tab_Scroll_Left.setSizePolicy(sizePolicy3)
        self.Tab_Scroll_Left.setMinimumSize(QSize(10, 40))
        self.Tab_Scroll_Left.setMaximumSize(QSize(20, 40))
        self.Tab_Scroll_Left.setBaseSize(QSize(10, 40))

        self.gridLayout_22.addWidget(self.Tab_Scroll_Left, 0, 1, 1, 1)

        self.label_19 = QLabel(self.IconS)
        self.label_19.setObjectName("label_19")

        self.gridLayout_22.addWidget(self.label_19, 3, 0, 1, 1)

        self.Ribbon_Scroll_Left = QPushButton(self.IconS)
        self.Ribbon_Scroll_Left.setObjectName("Ribbon_Scroll_Left")
        sizePolicy3.setHeightForWidth(self.Ribbon_Scroll_Left.sizePolicy().hasHeightForWidth())
        self.Ribbon_Scroll_Left.setSizePolicy(sizePolicy3)
        self.Ribbon_Scroll_Left.setMinimumSize(QSize(20, 60))
        self.Ribbon_Scroll_Left.setMaximumSize(QSize(20, 60))

        self.gridLayout_22.addWidget(self.Ribbon_Scroll_Left, 2, 1, 1, 1)

        self.Tab_Scroll_Right = QPushButton(self.IconS)
        self.Tab_Scroll_Right.setObjectName("Tab_Scroll_Right")
        sizePolicy3.setHeightForWidth(self.Tab_Scroll_Right.sizePolicy().hasHeightForWidth())
        self.Tab_Scroll_Right.setSizePolicy(sizePolicy3)
        self.Tab_Scroll_Right.setMinimumSize(QSize(10, 40))
        self.Tab_Scroll_Right.setMaximumSize(QSize(20, 40))
        self.Tab_Scroll_Right.setBaseSize(QSize(10, 40))

        self.gridLayout_22.addWidget(self.Tab_Scroll_Right, 1, 1, 1, 1)

        self.Ribbon_Scroll_Right = QPushButton(self.IconS)
        self.Ribbon_Scroll_Right.setObjectName("Ribbon_Scroll_Right")
        sizePolicy3.setHeightForWidth(self.Ribbon_Scroll_Right.sizePolicy().hasHeightForWidth())
        self.Ribbon_Scroll_Right.setSizePolicy(sizePolicy3)
        self.Ribbon_Scroll_Right.setMinimumSize(QSize(20, 60))
        self.Ribbon_Scroll_Right.setMaximumSize(QSize(20, 60))

        self.gridLayout_22.addWidget(self.Ribbon_Scroll_Right, 3, 1, 1, 1)

        self.label_16 = QLabel(self.IconS)
        self.label_16.setObjectName("label_16")

        self.gridLayout_22.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_17 = QLabel(self.IconS)
        self.label_17.setObjectName("label_17")

        self.gridLayout_22.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_18 = QLabel(self.IconS)
        self.label_18.setObjectName("label_18")

        self.gridLayout_22.addWidget(self.label_18, 2, 0, 1, 1)

        self.label_20 = QLabel(self.IconS)
        self.label_20.setObjectName("label_20")

        self.gridLayout_22.addWidget(self.label_20, 4, 0, 1, 1)

        self.MoreCommands = QPushButton(self.IconS)
        self.MoreCommands.setObjectName("MoreCommands")
        sizePolicy3.setHeightForWidth(self.MoreCommands.sizePolicy().hasHeightForWidth())
        self.MoreCommands.setSizePolicy(sizePolicy3)
        self.MoreCommands.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_22.addWidget(self.MoreCommands, 4, 1, 1, 1)

        self.gridLayout_23.addWidget(self.IconS, 1, 0, 1, 1)

        self.gridLayout_19.addWidget(self.groupBox_9, 1, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_21 = QGridLayout(self.groupBox_8)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.CustomColors = QCheckBox(self.groupBox_8)
        self.CustomColors.setObjectName("CustomColors")

        self.gridLayout_21.addWidget(self.CustomColors, 0, 0, 1, 1)

        self.ColorS = QGroupBox(self.groupBox_8)
        self.ColorS.setObjectName("ColorS")
        self.ColorS.setEnabled(False)
        self.gridLayout_20 = QGridLayout(self.ColorS)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.label_9 = QLabel(self.ColorS)
        self.label_9.setObjectName("label_9")
        self.label_9.setWordWrap(True)

        self.gridLayout_20.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_8 = QLabel(self.ColorS)
        self.label_8.setObjectName("label_8")
        self.label_8.setMinimumSize(QSize(200, 40))
        self.label_8.setWordWrap(True)

        self.gridLayout_20.addWidget(self.label_8, 1, 0, 1, 1)

        self.Color_Background = Gui_PrefColorButton(self.ColorS)
        self.Color_Background.setObjectName("Color_Background")
        sizePolicy3.setHeightForWidth(self.Color_Background.sizePolicy().hasHeightForWidth())
        self.Color_Background.setSizePolicy(sizePolicy3)

        self.gridLayout_20.addWidget(self.Color_Background, 1, 1, 1, 1)

        self.Color_Borders = Gui_PrefColorButton(self.ColorS)
        self.Color_Borders.setObjectName("Color_Borders")
        sizePolicy3.setHeightForWidth(self.Color_Borders.sizePolicy().hasHeightForWidth())
        self.Color_Borders.setSizePolicy(sizePolicy3)

        self.gridLayout_20.addWidget(self.Color_Borders, 0, 1, 1, 1)

        self.label_6 = QLabel(self.ColorS)
        self.label_6.setObjectName("label_6")

        self.gridLayout_20.addWidget(self.label_6, 0, 0, 1, 1)

        self.Color_Background_App = Gui_ColorButton(self.ColorS)
        self.Color_Background_App.setObjectName("Color_Background_App")
        sizePolicy3.setHeightForWidth(self.Color_Background_App.sizePolicy().hasHeightForWidth())
        self.Color_Background_App.setSizePolicy(sizePolicy3)

        self.gridLayout_20.addWidget(self.Color_Background_App, 2, 1, 1, 1)

        self.gridLayout_21.addWidget(self.ColorS, 1, 0, 1, 1)

        self.gridLayout_19.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.EnableBackup.toggled.connect(self.groupBox_Backup.setEnabled)
        self.CustomColors.toggled.connect(self.ColorS.setEnabled)
        self.CustomIcons.toggled.connect(self.IconS.setEnabled)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.Cancel.setText(QCoreApplication.translate("Form", "Cancel", None))
        # if QT_CONFIG(shortcut)
        self.Cancel.setShortcut(QCoreApplication.translate("Form", "Esc", None))
        # endif // QT_CONFIG(shortcut)
        self.GenerateJsonExit.setText(QCoreApplication.translate("Form", "Close", None))
        # if QT_CONFIG(shortcut)
        self.GenerateJsonExit.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.DebugMode.setText(QCoreApplication.translate("Form", "Debug mode", None))
        self.label_3.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p><span style=" font-style:italic;">Debug mode enables extra reports in the report view for debugging purposes.</span></p></body></html>',
                None,
            )
        )
        self.groupBox.setTitle(QCoreApplication.translate("Form", "Ribbon settings", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", "Show text", None))
        self.ShowText_Small.setText(QCoreApplication.translate("Form", "Small buttons", None))
        self.ShowText_Medium.setText(QCoreApplication.translate("Form", "Medium buttons", None))
        self.ShowText_Large.setText(QCoreApplication.translate("Form", "Large buttons", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", "Button size", None))
        self.label_11.setText(QCoreApplication.translate("Form", "Size of medium buttons:", None))
        self.label_10.setText(QCoreApplication.translate("Form", "Size of small buttons:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", "Panels", None))
        self.label.setText(QCoreApplication.translate("Form", "No. of columns per panel", None))
        self.label_2.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p><span style=\" font-style:italic;\">Set to '0'  to disable the maximum of columns</span></p></body></html>",
                None,
            )
        )
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", "Select stylesheet", None))
        self.label_7.setText(QCoreApplication.translate("Form", "...\\", None))
        self.StyleSheetLocation.setText(QCoreApplication.translate("Form", "Browse..", None))
        self.groupBox1.setTitle(QCoreApplication.translate("Form", "Backup settings", None))
        self.EnableBackup.setText(QCoreApplication.translate("Form", "Create backup", None))
        self.groupBox_Backup.setTitle(QCoreApplication.translate("Form", "Backup location", None))
        self.label_4.setText(QCoreApplication.translate("Form", "...\\", None))
        self.BackUpLocation.setText(QCoreApplication.translate("Form", "Browse..", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.General), QCoreApplication.translate("Form", "General", None)
        )
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", "Scroll buttons", None))
        self.label_14.setText(
            QCoreApplication.translate(
                "Form", "<html><head/><body><p>Scroll steps per click for ribbon:</p></body></html>", None
            )
        )
        self.label_15.setText(
            QCoreApplication.translate(
                "Form", "<html><head/><body><p>Scroll steps per click for tab bar:</p></body></html>", None
            )
        )
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", "Mouse settings", None))
        self.EnableEnterEvent.setText(QCoreApplication.translate("Form", "Show ribbon on hover. ", None))
        self.label_12.setText(
            QCoreApplication.translate("Form", "<html><head/><body><p>Scroll speed for ribbon:</p></body></html>", None)
        )
        self.label_13.setText(
            QCoreApplication.translate(
                "Form", "<html><head/><body><p>Scroll speed for tab bar:</p></body></html>", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", "Navigation", None)
        )
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", "Icons", None))
        self.CustomIcons.setText(QCoreApplication.translate("Form", "Enable custom icons", None))
        self.Tab_Scroll_Left.setText(QCoreApplication.translate("Form", "...", None))
        self.label_19.setText(
            QCoreApplication.translate("Form", "<html><head/><body><p>Ribbon bar scroll right:</p></body></html>", None)
        )
        self.Ribbon_Scroll_Left.setText(QCoreApplication.translate("Form", "...", None))
        self.Tab_Scroll_Right.setText(QCoreApplication.translate("Form", "...", None))
        self.Ribbon_Scroll_Right.setText(QCoreApplication.translate("Form", "...", None))
        self.label_16.setText(
            QCoreApplication.translate("Form", "<html><head/><body><p>Tab bar scroll left:</p></body></html>", None)
        )
        self.label_17.setText(QCoreApplication.translate("Form", "Tab bar scroll right:", None))
        self.label_18.setText(QCoreApplication.translate("Form", "Ribbon bar scroll left:", None))
        self.label_20.setText(
            QCoreApplication.translate("Form", "<html><head/><body><p>More commands button:</p></body></html>", None)
        )
        self.MoreCommands.setText(QCoreApplication.translate("Form", "...", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Form", "Colors", None))
        self.CustomColors.setText(QCoreApplication.translate("Form", "Enable custom colors", None))
        self.label_9.setText(
            QCoreApplication.translate("Form", "Set the background color for the application button:", None)
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>Set the background color for the controls and toolbars:</p></body></html>",
                None,
            )
        )
        self.label_6.setText(QCoreApplication.translate("Form", "Set the color for control borders:", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", "Colors and icons", None)
        )

    # retranslateUi
