# Copyright 2025 Canonical
# See LICENSE file for licensing details.

from unittest.mock import patch

from transition import NGINX_SITE_CONFIG_PATH, Transition


@patch("transition.Path.unlink")
@patch("transition.shutil.copy")
@patch.object(Transition, "_install_packages")
@patch("transition.SRVDIR")
def test_install_updates_charm_files_on_upgrade(
    srvdir_mock,
    install_packages_mock,
    copy_mock,
    unlink_mock,
):
    srvdir_mock.is_dir.return_value = True

    Transition().install()

    install_packages_mock.assert_called_once_with()
    srvdir_mock.is_dir.assert_called_once_with()
    copy_mock.assert_any_call("src/script/syncmirror", "/usr/bin")
    copy_mock.assert_any_call("src/nginx/transition.conf", NGINX_SITE_CONFIG_PATH)
    unlink_mock.assert_called_once_with(missing_ok=True)
