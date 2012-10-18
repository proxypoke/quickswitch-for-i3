# Maintainer: slowpoke <mail+aur at slowpoke dot io>
pkgname='quickswitch-i3'
pkgver=1.0
pkgrel=2
pkgdesc="quickly change to and locate windows in i3"
arch=(any)
url="https://github.com/proxypoke/quickswitch-for-i3"
license=('WTFPL')
groups=()
depends=('i3-wm' 'python' 'i3-py-git' 'dmenu')
makedepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install=
source=('http://pypi.python.org/packages/source/q/quickswitch-i3/quickswitch-i3-1.0.tar.gz')
md5sums=('255e07357ffdac11dd5730f9cdacfe97')

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
