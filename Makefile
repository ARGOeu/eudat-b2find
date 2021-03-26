PKGNAME=eudat-b2find
SPECFILE=${PKGNAME}.spec
FILES=Makefile ${SPECFILE} checkB2FIND.sh

PKGVERSION=$(shell grep -s '^Version:' $(SPECFILE) | sed -e 's/Version:\s*//')


dist:
	rm -rf dist
	mkdir -p dist/${PKGNAME}-${PKGVERSION}
	cp -pr ${FILES} dist/${PKGNAME}-${PKGVERSION}/.
	cd dist ; tar cfz ../${PKGNAME}-${PKGVERSION}.tar.gz ${PKGNAME}-${PKGVERSION}
	rm -rf dist

sources: dist

clean:
	rm -rf ${PKGNAME}-${PKGVERSION}.tar.gz
	rm -rf dist

