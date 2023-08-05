﻿import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class Forms2OleControl(aspose.words.drawing.ole.OleControl):
    '''Represents Microsoft Forms 2.0 OLE control.'''
    
    @property
    def caption(self) -> str:
        '''Gets Caption property of control. Default value is an empty string.'''
        ...
    
    @property
    def value(self) -> str:
        '''Gets underlying Value property which often represents control state.
        For example checked option button has '1' value while unchecked has '0'.
        Default value is an empty string.'''
        ...
    
    @property
    def enabled(self) -> bool:
        '''Returns true if control is in enabled state.'''
        ...
    
    @property
    def child_nodes(self) -> aspose.words.drawing.ole.Forms2OleControlCollection:
        '''Gets collection of immediate child controls.
        
        Returns **null** if this control can not have children.'''
        ...
    
    @property
    def type(self) -> aspose.words.drawing.ole.Forms2OleControlType:
        '''Gets type of Forms 2.0 control.'''
        ...
    
    ...

class Forms2OleControlCollection:
    '''Represents collection of :class:`Forms2OleControl` objects.'''
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> aspose.words.drawing.ole.Forms2OleControl:
        '''Gets :class:`Forms2OleControl` object at specified index.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets count of objects in the collection.'''
        ...
    
    ...

class OleControl:
    '''Represents OLE ActiveX control.'''
    
    def as_forms2_ole_control(self) -> aspose.words.drawing.ole.Forms2OleControl:
        ...
    
    @property
    def is_forms2_ole_control(self) -> bool:
        '''Returns true if the control is a :class:`Forms2OleControl`.'''
        ...
    
    @property
    def name(self) -> str:
        '''Gets name of the ActiveX control.'''
        ...
    
    ...

class Forms2OleControlType:
    
    OPTION_BUTTON: int
    LABEL: int
    TEXTBOX: int
    CHECK_BOX: int
    TOGGLE_BUTTON: int
    SPIN_BUTTON: int
    COMBO_BOX: int
    FRAME: int
    MULTI_PAGE: int
    TAB_STRIP: int
    COMMAND_BUTTON: int
    IMAGE: int
    SCROLL_BAR: int
    FORM: int
    LIST_BOX: int

