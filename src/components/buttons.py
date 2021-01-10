from kivy.properties import (
    BooleanProperty,  # @UnresolvedImport
    StringProperty,  # @UnresolvedImport
    NumericProperty,  # @UnresolvedImport
    BoundedNumericProperty,  # @UnresolvedImport
)
from kivymd.uix.button import (
    BaseButton,
    BaseElevationButton,
    BasePressedButton,
    MDFloatingActionButton,
    MDIconButton,
    MDFlatButton,
)
from kivymd.uix.behaviors import CircularRippleBehavior, RectangularRippleBehavior
from kivymd.uix.behaviors.elevation import RectangularElevationBehavior
from kivymd.uix.behaviors.backgroundcolor_behavior import SpecificBackgroundColorBehavior

#------------------------------------------------------------------------------

class CustomRectangularButton(RectangularRippleBehavior, BaseButton):
    width = BoundedNumericProperty(
        10, min=10, max=None, errorhandler=lambda x: 10
    )
    text = StringProperty("")
    increment_width = NumericProperty("0dp")
    button_label = BooleanProperty(True)
    can_capitalize = BooleanProperty(True)
    _radius = NumericProperty("2dp")
    _height = NumericProperty(0)
    text_halign = StringProperty('center')


class CustomRoundButton(CircularRippleBehavior, BaseButton):
    increment_diameter = NumericProperty(12)
    ripple_scale = 10
    _radius = 0


class CustomRectangularIconButton(RectangularRippleBehavior, BaseButton):
    increment_width = NumericProperty("0dp")
    _radius = NumericProperty("2dp")


# class CustomFlatButton(CustomRectangularButton, BaseFlatButton, BasePressedButton):
#     width = BoundedNumericProperty(
#         10, min=10, max=None, errorhandler=lambda x: 10
#     )
#     increment_width = 0

class CustomFlatButton(MDFlatButton):
    pass


class CustomRaisedButton(CustomRectangularButton, RectangularElevationBehavior, SpecificBackgroundColorBehavior, BaseElevationButton, BasePressedButton):
    pass


class CustomFloatingActionButton(SpecificBackgroundColorBehavior, MDFloatingActionButton):
    button_size = NumericProperty('32dp')

    def set_size(self, interval):
        self.width = self.button_size
        self.height = self.button_size


class RoundedButton(CustomRaisedButton):
    pass


class RoundedFlexWidthButton(RoundedButton):
    pass


class RoundedFlexHeightButton(RoundedButton):
    pass


class RoundedFlexButton(RoundedButton):
    pass


class IconButton(SpecificBackgroundColorBehavior, MDIconButton):
    button_size = NumericProperty('32dp')

    def set_size(self, interval):
        self.width = self.button_size
        self.height = self.button_size


class RaisedIconButton(CustomRectangularIconButton, RectangularElevationBehavior, SpecificBackgroundColorBehavior, BaseElevationButton, BasePressedButton):
    icon = StringProperty("circle")


class CustomIconButton(IconButton):
    pass


class CloseIconButton(IconButton):
    pass


class CustomRaisedIconButton(RaisedIconButton):
    pass

#------------------------------------------------------------------------------

from kivy.lang.builder import Builder 
Builder.load_file('./components/buttons.kv')
