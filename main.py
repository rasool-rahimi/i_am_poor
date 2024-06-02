import flet as ft


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("Poor App"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False,
                    ),
                ]
            ),
        ],
    )

    page.add(
        ft.Image(
            src="/images/poor.png",
            width=300,
            border_radius=30
        ),

        ft.Container(height=20),

        ft.Text(
            value="I am poor",
            size=50
        )
    )


ft.app(target=main, assets_dir="assets")
